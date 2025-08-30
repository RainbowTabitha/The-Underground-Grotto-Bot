#***************************************************************************#
# FloofBot
#***************************************************************************#

import discord
from discord.ext import commands
import json
import os

# Files for bot data and configuration
DB_FILE = 'db.json'
CONFIG_FILE = 'config.json'

# Load configuration data
def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def get_setting(key, default=None):
    config = load_config()
    return config.get(key, default)

# Load or initialize database data
def load_db():
    if not os.path.exists(DB_FILE):
        return {"quotes": [], "birthdays": {}, "levels": {}}
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Load levels data from unified database
def load_levels():
    data = load_db()
    return data.get('levels', {})

def save_levels(levels_data):
    data = load_db()
    data['levels'] = levels_data
    save_db(data)

# Initialize levels data
levels_data = load_levels()

# Function to calculate XP needed for the next level
def xp_needed(level):
    return ((500 * level) // 2)

class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        guild_id = str(message.guild.id)
        user_id = str(message.author.id)

        # Initialize the guild data if it doesn't exist
        if guild_id not in levels_data:
            levels_data[guild_id] = {}

        # Initialize user data if it doesn't exist
        if user_id not in levels_data[guild_id]:
            levels_data[guild_id][user_id] = {"level": 1, "xp": 0}

        # Award XP for sending a message
        xp_per_message = get_setting('xp_per_message', 10)
        levels_data[guild_id][user_id]["xp"] += xp_per_message

        # Check for level up
        current_level = levels_data[guild_id][user_id]["level"]
        if levels_data[guild_id][user_id]["xp"] >= xp_needed(current_level):
            levels_data[guild_id][user_id]["level"] += 1
            levels_data[guild_id][user_id]["xp"] = 0  # Reset XP or adjust as needed
            
            # Create an embed for the level-up message
            embed = discord.Embed(
                title="Level Up!",
                description=f"Congratulations {message.author.mention}, you've leveled up to level {levels_data[guild_id][user_id]['level']}!",
                color=discord.Color.green()
            )
            embed.set_thumbnail(url=message.author.avatar.url)  # User's profile picture
            embed.set_footer(text=f"Keep being active, {message.author.name}, to reach the next level!")  # User's name in footer

            await message.channel.send(embed=embed)

        # Save levels data after each message
        save_levels(levels_data)

    @commands.slash_command()
    async def level(self, ctx: discord.ApplicationContext):
        """Check your current level and XP."""
        guild_id = str(ctx.guild.id)  # Get the server (guild) ID
        user_id = str(ctx.author.id)

        if guild_id in levels_data and user_id in levels_data[guild_id]:
            level = levels_data[guild_id][user_id]["level"]
            xp = levels_data[guild_id][user_id]["xp"]
            await ctx.respond(f"{ctx.author.mention}, you are currently level {level} with {xp} XP.")
        else:
            await ctx.respond(f"{ctx.author.mention}, you have not gained any XP yet.")

    @commands.slash_command()
    async def leaderboard(self, ctx: discord.ApplicationContext):
        """Display the leaderboard of users by level with pagination."""
        guild_id = str(ctx.guild.id)  # Get the server (guild) ID
 
        if guild_id not in levels_data or not levels_data[guild_id]:
            await ctx.respond("No users have gained levels yet.")
            return
 
        # Create a list of users and their levels
        leaderboard = []
        for user_id, data in levels_data[guild_id].items():
            leaderboard.append((user_id, data["level"], data["xp"]))
 
        # Sort the leaderboard by level and XP
        leaderboard.sort(key=lambda x: (x[1], x[2]), reverse=True)

        # Assign ranks
        ranked_leaderboard = []
        current_rank = 1
        previous_level = None
        previous_xp = None

        for index, (user_id, level, xp) in enumerate(leaderboard):
            if (level, xp) != (previous_level, previous_xp):
                current_rank = index + 1  # Update rank only if the level and XP change
            ranked_leaderboard.append((user_id, current_rank, level, xp))  # Store user_id, rank, level, and XP
            previous_level, previous_xp = level, xp  # Update previous_level and previous_xp for the next iteration

        # Pagination logic
        page_size = 10
        total_pages = (len(ranked_leaderboard) + page_size - 1) // page_size  # Calculate total pages
        current_page = 0
 
        # Function to create and send the embed for the current page
        async def send_leaderboard_page(page):
            embed = discord.Embed(title="Leaderboard", color=discord.Color.blue())
            start_index = page * page_size
            end_index = start_index + page_size
            for index, (user_id, rank, level, xp) in enumerate(ranked_leaderboard[start_index:end_index], start=start_index + 1):
                user = ctx.guild.get_member(int(user_id))
                username = user.display_name if user else "Unknown User"
                embed.add_field(name=f"{rank}. {username}", value=f"Level: {level}, XP: {xp}", inline=False)
            embed.set_footer(text=f"Page {page + 1}/{total_pages}")
            return embed
 
        # Send the initial message with the leaderboard
        message = await ctx.respond("Here is the leaderboard:", embed=await send_leaderboard_page(current_page))
        message = await message.original_message()

        # Add reactions for pagination
        if total_pages > 1:
            await message.add_reaction("◀️")  # Previous page
            await message.add_reaction("▶️")  # Next page

        # Reaction handling
        async def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"] and reaction.message.id == message.id

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60.0, check=check)
                if str(reaction.emoji) == "◀️" and current_page > 0:
                    current_page -= 1
                    await message.edit(embed=await send_leaderboard_page(current_page))
                elif str(reaction.emoji) == "▶️" and current_page < total_pages - 1:
                    current_page += 1
                    await message.edit(embed=await send_leaderboard_page(current_page))

                # Remove the user's reaction
                await message.remove_reaction(reaction, user)

            except Exception as e:
                print(f"Error during reaction handling: {e}")
                break  # Exit the loop on timeout or error

    @commands.slash_command()
    @commands.has_role("STAFF")
    async def retroactive_roles(self, ctx: discord.ApplicationContext):
        """Retroactively assign roles to users who meet the level requirements."""
        guild_id = str(ctx.guild.id)
        level_roles = get_setting('level_roles', {})
        
        if not level_roles:
            await ctx.respond("No level roles configured.")
            return
            
        if guild_id not in levels_data:
            await ctx.respond("No level data exists for this server.")
            return
            
        assigned_count = 0
        for role_key, role_config in level_roles.items():
            role_name = role_config.get('name', '')
            required_level = role_config.get('required_level', 0)
            
            role = discord.utils.get(ctx.guild.roles, name=role_name)
            if not role:
                await ctx.respond(f"Error: The role '{role_name}' does not exist.")
                continue
                
            for user_id, data in levels_data[guild_id].items():
                if data["level"] >= required_level:
                    member = ctx.guild.get_member(int(user_id))
                    if member and role not in member.roles:
                        await member.add_roles(role)
                        assigned_count += 1
                    
        await ctx.respond(f"Successfully assigned roles to {assigned_count} members based on their levels.")