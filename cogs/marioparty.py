#***************************************************************************#
#                                                                           #
# Underground Grotto Bot                                                    #
# Mario Party Commands                                                      #
# Copyright (C) 2024-2025 Tabitha Hanegan. All rights reserved.            #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#

import discord
import urllib
import asyncio
from discord.ext import commands
from discord import SlashCommandGroup
from util.wheel import generate_wheel_gif

class MarioParty(commands.Cog):

    """Cog for Mario Party commands"""

    def __init__(self, bot):
        self.bot = bot

    board = SlashCommandGroup("board", "MP Board related commands")
    partyplanner = SlashCommandGroup("partyplanner", "Party Planner related commands")

    async def spin_wheel_and_show_result(self, ctx, options, title, description, image_path=None, filename=None):
        """Generic function to spin wheel and show result with embed."""
        # Use the wheel system
        selected, gif_io, _ = generate_wheel_gif(options)
        
        await ctx.respond(f"Spinning for {description.lower()}...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)

        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()
        
        # Create embed
        result_embed = discord.Embed(title=title, description=f"**{selected}**", colour=0x98FB98)
        
        # Add image if provided
        if image_path and filename:
            try:
                file = discord.File(image_path, filename=filename)
                result_embed.set_image(url=f"attachment://{filename}")
                result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, The Underground Grotto Bot")
                await ctx.send(embed=result_embed, file=file)
            except FileNotFoundError:
                result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, The Underground Grotto Bot")
                await ctx.send(embed=result_embed)
        else:
            result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, The Underground Grotto Bot")
            await ctx.send(embed=result_embed)

    # Game selection commands
    @commands.slash_command(name="pickgame", description="Random Mario Party game")
    async def pickgame(self, ctx):
        games = [f"Mario Party {i}" for i in range(1, 9)]
        selected, gif_io, _ = generate_wheel_gif(games)
        await self.spin_wheel_and_show_result(ctx, games, "🎮 Mario Party Game Selected!", "Mario Party game",
                                             f"assets/MP{int(selected.split()[-1])}.png", f"MP{int(selected.split()[-1])}.png")

    @commands.slash_command(name="pickgcwii", description="Random GC/Wii Mario Party game")
    async def pickgcwii(self, ctx):
        games = [f"Mario Party {i}" for i in range(4, 9)]
        selected, gif_io, _ = generate_wheel_gif(games)
        await self.spin_wheel_and_show_result(ctx, games, "🎮 GC/Wii Mario Party Game Selected!", "GC/Wii Mario Party game",
                                             f"assets/MP{int(selected.split()[-1])}.png", f"MP{int(selected.split()[-1])}.png")

    @commands.slash_command(name="pickn64", description="Random N64 Mario Party game")
    async def pickn64(self, ctx):
        games = [f"Mario Party {i}" for i in range(1, 4)]
        selected, gif_io, _ = generate_wheel_gif(games)
        await self.spin_wheel_and_show_result(ctx, games, "🎮 N64 Mario Party Game Selected!", "N64 Mario Party game",
                                             f"assets/MP{int(selected.split()[-1])}.png", f"MP{int(selected.split()[-1])}.png")

    # Game mode commands
    @commands.slash_command(name="picknormalgamemode", description="Random normal game mode")
    async def picknormalgamemode(self, ctx):
        modes = ["Mario Party: Magic Conch", "Mario Party: Simon Says", "Mario Party: Raiders Wrath", "Mario Party: Inversal Reversal"]
        selected, gif_io, _ = generate_wheel_gif(modes)
        await self.spin_wheel_and_show_result(ctx, modes, "🎯 Normal Game Mode Selected!", "normal game mode")

    @commands.slash_command(name="pickmayhemgamemode", description="Random mayhem game mode")
    async def pickmayhemgamemode(self, ctx):
        modes = [
            "Mario Party Mayhem: Classic", "Mario Party Mayhem: Modern", "Mario Party Mayhem: Magic Conch",
            "Mario Party Mayhem: Mayhem Says", "Mario Party Mayhem: Raiders Wrath", "Mario Party Mayhem: Inversal Reversal"
        ]
        selected, gif_io, _ = generate_wheel_gif(modes)
        await self.spin_wheel_and_show_result(ctx, modes, "🎯 Mayhem Game Mode Selected!", "mayhem game mode")

    @commands.slash_command(name="pickmp4mode", description="Random Mario Party 4 version")
    async def pickMP4mode(self, ctx):
        modes = ["Vanilla", "DX"]
        selected, gif_io, _ = generate_wheel_gif(modes)
        await self.spin_wheel_and_show_result(ctx, modes, "🎯 Mario Party 4 Version Selected!", "MP4 version")

    @commands.slash_command(name="pickmpmode", description="Random Mario Party mode")
    async def pickMPmode(self, ctx):
        modes = ["Vanilla", "Mayhem"]
        selected, gif_io, _ = generate_wheel_gif(modes)
        await self.spin_wheel_and_show_result(ctx, modes, "🎮 Mario Party Mode Selected!", "Mario Party mode")

    # Settings commands
    @commands.slash_command(name="bonusstars", description="Random bonus stars setting")
    async def bstars(self, ctx):
        options = ["Off", "On", "Ztars"]
        selected, gif_io, _ = generate_wheel_gif(options)
        await self.spin_wheel_and_show_result(ctx, options, "⭐ Bonus Stars Setting Selected!", "bonus stars setting")

    @commands.slash_command(name="duels", description="Random duels setting")
    async def duels(self, ctx):
        options = ["Always", "Vanilla", "Never"]
        selected, gif_io, _ = generate_wheel_gif(options)
        await self.spin_wheel_and_show_result(ctx, options, "⚔️ Same Space Duels Setting Selected!", "duels setting")

    @commands.slash_command(name="gentlemans", description="Random gentleman's rule setting")
    async def gentlemans(self, ctx):
        options = ["On", "Off"]
        selected, gif_io, _ = generate_wheel_gif(options)
        await self.spin_wheel_and_show_result(ctx, options, "🎩 Gentleman's Rule Setting Selected!", "gentleman's rule setting")

    @commands.slash_command(name='wheel', description="Spin a wheel with optional args")
    async def wheel(self, ctx, args: str = None):
        if not args:
            await ctx.respond("Please provide options separated by commas. Example: `/wheel Mario Party 1, Mario Party 2, Mario Party 3`")
            return
            
        filter_options = [option.strip() for option in args.split(',')]
        await ctx.respond(f"🎯 Filtering wheel options to: {', '.join(filter_options)}")

        selected, gif_io, _ = generate_wheel_gif(filter_options)
        await self.spin_wheel_and_show_result(ctx, filter_options, f"🎉 The wheel landed on: {selected}!", "wheel selection")

    async def spin_board_wheel(self, ctx, boardList, game_name):
        """Helper function to spin the wheel for any Mario Party game board."""
        # Generate GIF & final static image
        selected_board, gif_io, final_img_io = generate_wheel_gif(boardList)
        
        await ctx.respond("Spinning...", delete_after=0)

        # Send the GIF
        gif_file = discord.File(gif_io, "spinning_wheel.gif")
        message = await ctx.send(file=gif_file)

        # Wait for suspense
        await asyncio.sleep(5)

        # Delete the GIF message
        await message.delete()

        # Send the final static image
        final_image_file = discord.File(final_img_io, "final_wheel.png")
        await ctx.send(file=final_image_file)

        # Send the embed separately
        result_embed = discord.Embed(title=f"🎉 The wheel landed on: {selected_board}!", colour=0x98FB98)
        result_embed.set_image(url="attachment://final_wheel.png")
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, The Underground Grotto Bot")

        await ctx.send(embed=result_embed, file=final_image_file)

    @board.command(name='1')
    async def one(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 1 board."""
        boardList = [
            "DK's Jungle Adventure", "Peach's Birthday Cake", "Yoshi's Tropical Island", 
            "Mario's Rainbow Castle", "Wario's Battle Canyon", "Luigi's Engine Room", 
            "Eternal Star", "Bowser's Magma Mountain"
        ]
        await self.spin_board_wheel(ctx, boardList, "1")

    @board.command(name='2')
    async def two(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 2 board."""
        boardList = [
            "Western Land", "Space Land", "Mystery Land", 
            "Pirate Land", "Horror Land", "Bowser Land"
        ]
        await self.spin_board_wheel(ctx, boardList, "2")

    @board.command(name='3')
    async def three(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 3 board."""
        boardList = [
            "Chilly Waters", "Deep Bloober Sea", "Woody Woods", 
            "Creepy Cavern", "Spiny Desert", "Waluigi's Island"
        ]
        await self.spin_board_wheel(ctx, boardList, "3")

    @board.command(name='4')
    async def four(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 4 board."""
        boardList = [
            "Toad's Midway Madness", "Boo's Haunted Bash", "Koopa's Seaside Soiree", 
            "Goomba's Greedy Gala", "Shy Guy's Jungle Jam", "Bowser's Gnarly Party"
        ]
        await self.spin_board_wheel(ctx, boardList, "4")

    @board.command(name='5')
    async def five(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 5 board."""
        boardList = [
            "Toy Dream", "Rainbow Dream", "Pirate Dream", 
            "Future Dream", "Undersea Dream", "Sweet Dream", "Bowser's Nightmare"
        ]
        await self.spin_board_wheel(ctx, boardList, "5")

    @board.command(name='6')
    async def six(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 6 board."""
        boardList = [
            "Towering Treetop", "E Gadd's Garage", "Faire Square", 
            "Snowflake Lake", "Castaway Bay", "Clockwork Castle"
        ]
        await self.spin_board_wheel(ctx, boardList, "6")

    @board.command(name='7')
    async def seven(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 7 board."""
        boardList = [
            "Grand Canal", "Pagoda Peak", "Pyramid Park", 
            "Neon Heights", "Windmillville", "Bowser's Enchanted Inferno"
        ]
        await self.spin_board_wheel(ctx, boardList, "7")

    @board.command(name='8')
    async def eight(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 8 board."""
        boardList = [
            "DK's Treetop Temple", "Goomba's Booty Boardwalk", "King Boo's Haunted Hideaway", 
            "Shy Guy's Perplex Express", "Koopa's Tycoon Town", "Bowser's Warped Orbit"
        ]
        await self.spin_board_wheel(ctx, boardList, "8")

    @board.command(name='9')
    async def nine(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 9 board."""
        boardList = [
            "Toad Road", "Blooper Beach", "Boo's Horror Castle", 
            "DK's Jungle Ruins", "Bowser's Station", "Magma Mine", "Bob-omb Factory"
        ]
        await self.spin_board_wheel(ctx, boardList, "9")

    @board.command(name='10')
    async def ten(self, ctx):
        """Spins a wheel to randomly pick a Mario Party 10 board."""
        boardList = ["Mushroom Park", "Whimsical Waters", "Chaos Castle", "Airship Central", "Haunted Trail"]
        await self.spin_board_wheel(ctx, boardList, "10")

    @board.command()
    async def ds(self, ctx):
        """Spins a wheel to randomly pick a Mario Party DS board."""
        boardList = ["Wiggler's Garden", "Kamek's Library", "Bowser's Pinball Machine", "Toadette's Music Room", "DK's Stone Statue"]
        await self.spin_board_wheel(ctx, boardList, "DS")

    @board.command(name='super')
    async def super(self, ctx):
        """Spins a wheel to randomly pick a Super Mario Party board."""
        boardList = ["Whomp's Domino Ruins", "King Bob-omb's Powderkeg Mine", "Megafruit Paradise", "Kamek's Tantalizing Tower"]
        await self.spin_board_wheel(ctx, boardList, "Super")

    @board.command(name='superstars')
    async def superstars(self, ctx):
        """Spins a wheel to randomly pick a Mario Party Superstars board."""
        boardList = ["Yoshi's Tropical Island", "Peach's Birthday Cake", 'Space Land', 'Horror Land', 'Woody Woods']
        await self.spin_board_wheel(ctx, boardList, "Superstars")

    @board.command(name='jamboree')
    async def jamboree(self, ctx):
        """Spins a wheel to randomly pick a Super Mario Party Jamboree board."""
        boardList = [
            "Mega Wiggler's Tree Party", "Rainbow Galleria", 'Goomba Lagoon', 
            "Roll\'em Raceway", 'Western Land', "Mario\'s Rainbow Castle", "King Bowser\'s Keep"
        ]
        await self.spin_board_wheel(ctx, boardList, "Jamboree")

def setup(bot):
    bot.add_cog(MarioParty(bot))