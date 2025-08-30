import discord
import logging
import os
import asyncio
import random
from datetime import datetime
from dotenv import load_dotenv
from wheel import generate_wheel_gif, spin_wheel_and_show_result

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Bot setup
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('discord.log', encoding='utf-8', mode='w'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('UndergroundGrottoBot')

def get_commands_list():
    """Automatically generate the list of available slash commands."""
    commands = []
    if hasattr(bot, 'application_commands'):
        for cmd in bot.application_commands:
            if hasattr(cmd, 'name'):
                commands.append(f"/{cmd.name}")
    return sorted(commands)

# Initialize empty commands list (will be populated after bot sync)
COMMANDS_LIST = []

def get_board_key_by_value(board_dict, value):
    """Get the key for a given board value."""
    for key, val in board_dict.items():
        if val == value:
            return key
    return None

# Bot events
@bot.event
async def on_ready():
    logger.info(f'Bot is ready! Logged in as {bot.user}')
    print(f'🎮 Now Running {bot.user}!')
    print(f'🆔 Bot ID: {bot.user.id}')
    print(f'📊 Connected to {len(bot.guilds)} guild(s)')
    print(f'👥 Serving {len(bot.users)} user(s)')
    
    try:
        synced = await bot.sync_commands()
        # Handle different return types from sync_commands()
        if synced is not None and hasattr(synced, '__len__'):
            logger.info(f"Synced {len(synced)} command(s)")
            print(f"✅ Synced {len(synced)} command(s)")
        else:
            logger.info("Synced commands successfully")
            print("✅ Synced commands successfully")
        global COMMANDS_LIST
        COMMANDS_LIST = get_commands_list()
        print(f"📋 Available commands: {COMMANDS_LIST}")
    except Exception as e:
        logger.error(f"Failed to sync commands: {e}")
        print(f"❌ Failed to sync commands: {e}")

@bot.event
async def on_guild_join(guild):
    """Log when bot joins a new guild"""
    logger.info(f"Joined guild: {guild.name} (ID: {guild.id})")
    print(f"🎉 Joined new guild: {guild.name}")

@bot.event
async def on_guild_remove(guild):
    """Log when bot leaves a guild"""
    logger.info(f"Left guild: {guild.name} (ID: {guild.id})")
    print(f"👋 Left guild: {guild.name}")

@bot.event
async def on_command_error(ctx, error):
    """Global error handler"""
    if isinstance(error, discord.ApplicationCommandInvokeError):
        logger.error(f"Command error in {ctx.command}: {error.original}")
        await ctx.respond(f"❌ An error occurred: {str(error.original)}", ephemeral=True)
    else:
        logger.error(f"Unexpected error: {error}")
        await ctx.respond("❌ An unexpected error occurred.", ephemeral=True)

# Board selection commands
@bot.slash_command(name="board1", description="Selects a random Mario Party 1 board using the wheel.")
async def board1(ctx):
    """Selects a random Mario Party 1 board using the wheel."""
    boards1 = ["DK's Jungle Adventure", "Peach's Birthday Cake", "Yoshi's Tropical Island", "Wario's Battle Canyon", "Luigi's Engine Room", "Mario's Rainbow Castle", "Bowser's Magma Mountain", "Eternal Star"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards1)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=boards1,
        title="🎯 Mario Party 1 Board Selected!",
        description="MP1 board",
        image_path=f"assets/{selected}.png",
        filename=f"{selected}.png"
    )

@bot.slash_command(name="board2", description="Selects a random Mario Party 2 board using the wheel.")
async def board2(ctx):
    """Selects a random Mario Party 2 board using the wheel."""
    boards2 = ["Pirate Land", "Western Land", "Space Land", "Mystery Land", "Horror Land", "Bowser Land"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards2)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=boards2,
        title="🎯 Mario Party 2 Board Selected!",
        description="MP2 board",
        image_path=f"assets/{selected}.png",
        filename=f"{selected}.png"
    )

@bot.slash_command(name="board3", description="Selects a random Mario Party 3 board using the wheel.")
async def board3(ctx):
    """Selects a random Mario Party 3 board using the wheel."""
    boards3 = ["Chilly Waters", "Deep Bloober Sea", "Spiny Desert", "Woody Woods", "Creepy Cavern", "Waluigi's Island"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards3)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=boards3,
        title="🎯 Mario Party 3 Board Selected!",
        description="MP3 board",
        image_path=f"assets/{selected}.png",
        filename=f"{selected}.png"
    )

@bot.slash_command(name="board4", description="Selects a random Mario Party 4 board using the wheel.")
async def board4(ctx):
    """Selects a random Mario Party 4 board using the wheel."""
    boards4 = ["Toad's Midway Madness", "Shy Guy's Jungle Jam", "Goomba's Greedy Gala", "Boo's Haunted Bash", "Koopa's Seaside Soiree", "Bowser's Gnarly Party"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards4)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=boards4,
        title="🎯 Mario Party 4 Board Selected!",
        description="MP4 board",
        image_path=f"assets/{selected}.png",
        filename=f"{selected}.png"
    )

@bot.slash_command(name="board5", description="Selects a random Mario Party 5 board using the wheel.")
async def board5(ctx):
    """Selects a random Mario Party 5 board using the wheel."""
    boards5 = ["Toy Dream", "Rainbow Dream", "Pirate Dream", "Undersea Dream", "Future Dream", "Sweet Dream", "Bowser's Nightmare"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards5)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=boards5,
        title="🎯 Mario Party 5 Board Selected!",
        description="MP5 board",
        image_path=f"assets/{selected}.png",
        filename=f"{selected}.png"
    )

@bot.slash_command(name="board6", description="Selects a random Mario Party 6 board using the wheel.")
async def board6(ctx):
    """Selects a random Mario Party 6 board using the wheel."""
    boards6 = ["Towering Treetop", "E.Gadd's Garage", "Faire Square", "Snowflake Lake", "Castaway Bay", "Clockwork Castle"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards6)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=boards6,
        title="🎯 Mario Party 6 Board Selected!",
        description="MP6 board",
        image_path=f"assets/{selected}.png",
        filename=f"{selected}.png"
    )

@bot.slash_command(name="board7", description="Selects a random Mario Party 7 board using the wheel.")
async def board7(ctx):
    """Selects a random Mario Party 7 board using the wheel."""
    boards7 = ["Grand Canal", "Pagoda Peak", "Pyramid Park", "Neon Heights", "Windmillville", "Bowser's Enchanted Inferno"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards7)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=boards7,
        title="🎯 Mario Party 7 Board Selected!",
        description="MP7 board",
        image_path=f"assets/{selected}.png",
        filename=f"{selected}.png"
    )

@bot.slash_command(name="board8", description="Selects a random Mario Party 8 board using the wheel.")
async def board8(ctx):
    """Selects a random Mario Party 8 board using the wheel."""
    boards8 = ["DK's Treetop Temple", "Goomba's Booty Boardwalk", "King Boo's Haunted Hideaway", "Shy Guy's Perplex Express", "Koopa's Tycoon Town", "Bowser's Warped Orbit"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards8)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=boards8,
        title="🎯 Mario Party 8 Board Selected!",
        description="MP8 board",
        image_path=f"assets/{selected}.png",
        filename=f"{selected}.png"
    )

# Game selection commands
@bot.slash_command(name="pickgame", description="Selects a random Mario Party game using the wheel.")
async def pickgame(ctx):
    """Selects a random Mario Party game using the wheel."""
    game_names = [f"Mario Party {i}" for i in range(1, 9)]
    selected, gif_io, _ = generate_wheel_gif(ctx, game_names)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=game_names,
        title="🎮 Mario Party Game Selected!",
        description="Mario Party game",
        image_path=f"assets/MP{int(selected.split()[-1])}.png",
        filename=f"MP{int(selected.split()[-1])}.png"
    )

@bot.slash_command(name="pickgcwii", description="Selects a random GameCube/Wii Mario Party game using the wheel.")
async def pickgcwii(ctx):
    """Selects a random GameCube/Wii Mario Party game using the wheel."""
    game_names = [f"Mario Party {i}" for i in range(4, 9)]
    selected, gif_io, _ = generate_wheel_gif(ctx, game_names)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=game_names,
        title="🎮 GC/Wii Mario Party Game Selected!",
        description="GC/Wii Mario Party game",
        image_path=f"assets/MP{int(selected.split()[-1])}.png",
        filename=f"MP{int(selected.split()[-1])}.png"
    )

@bot.slash_command(name="pickn64", description="Selects a random N64 Mario Party game using the wheel.")
async def pickn64(ctx):
    """Selects a random N64 Mario Party game using the wheel."""
    game_names = [f"Mario Party {i}" for i in range(1, 4)]
    selected, gif_io, _ = generate_wheel_gif(ctx, game_names)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=game_names,
        title="🎮 N64 Mario Party Game Selected!",
        description="N64 Mario Party game",
        image_path=f"assets/MP{int(selected.split()[-1])}.png",
        filename=f"MP{int(selected.split()[-1])}.png"
    )

# Game mode commands
@bot.slash_command(name="picknormalgamemode", description="Selects a random normal game mode using the wheel.")
async def picknormalgamemode(ctx):
    """Selects a random normal game mode using the wheel."""
    normalgamemode = ["Mario Party: Magic Conch", "Mario Party: Simon Says", "Mario Party: Raiders Wrath", "Mario Party: Inversal Reversal"]
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(normalgamemode.values()),
        title="🎯 Normal Game Mode Selected!",
        description="normal game mode"
    )

@bot.slash_command(name="pickmayhemgamemode", description="Selects a random mayhem game mode using the wheel.")
async def pickmayhemgamemode(ctx):
    """Selects a random mayhem game mode using the wheel."""
    mayhemgamemode = ["Mario Party Mayhem: Classic", "Mario Party Mayhem: Modern", "Mario Party Mayhem: Magic Conch", "Mario Party Mayhem: Mayhem Says", "Mario Party Mayhem: Raiders Wrath", "Mario Party Mayhem: Inversal Reversal"]
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(mayhemgamemode.values()),
        title="🎯 Mayhem Game Mode Selected!",
        description="mayhem game mode"
    )

@bot.slash_command(name="pickmp4mode", description="Selects a random Mario Party 4 version using the wheel.")
async def pickMP4mode(ctx):
    """Selects a random Mario Party 4 version using the wheel."""
    mp4_versions = ["Vanilla", "DX"]
    selected, gif_io, _ = generate_wheel_gif(ctx, mp4_versions)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=mp4_versions,
        title="🎯 Mario Party 4 Version Selected!",
        description="MP4 version"
    )

@bot.slash_command(name="pickmpmode", description="Selects a random Mario Party mode using the wheel.")
async def pickMPmode(ctx):
    """Selects a random Mario Party mode using the wheel."""
    mp_modes = ["Vanilla", "Mayhem"]
    selected, gif_io, _ = generate_wheel_gif(ctx, mp_modes)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=mp_modes,
        title="🎮 Mario Party Mode Selected!",
        description="Mario Party mode"
    )

# Settings commands
@bot.slash_command(name="bonusstars", description="Selects a random bonus stars setting using the wheel.")
async def bstars(ctx):
    """Selects a random bonus stars setting using the wheel."""
    bonus_options = ["Off", "On", "Ztars"]
    selected, gif_io, _ = generate_wheel_gif(ctx, bonus_options)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=bonus_options,
        title="⭐ Bonus Stars Setting Selected!",
        description="bonus stars setting"
    )

@bot.slash_command(name="duels", description="Selects a random duels setting using the wheel.")
async def duels(ctx):
    """Selects a random duels setting using the wheel."""
    duels_options = ["Always", "Vanilla", "Never"]
    selected, gif_io, _ = generate_wheel_gif(ctx, duels_options)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=duels_options,
        title="⚔️ Same Space Duels Setting Selected!",
        description="duels setting"
    )

@bot.slash_command(name="gentlemans", description="Selects a random gentleman's rule setting using the wheel.")
async def gentlemans(ctx):
    """Selects a random gentleman's rule setting using the wheel."""
    gentleman_options = ["On", "Off"]
    selected, gif_io, _ = generate_wheel_gif(ctx, gentleman_options)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=gentleman_options,
        title="🎩 Gentleman's Rule Setting Selected!",
        description="gentleman's rule setting"
    )

# Utility commands
@bot.slash_command(name="commands", description="Shows the list of available commands.")
async def commands(ctx):
    """Shows the list of available commands."""
    commands_string = "\n".join(get_commands_list())
    await ctx.respond("## Here's The List of Commands!")
    await ctx.respond(commands_string)

@bot.slash_command(name='wheel', description="Spins a wheel with optional comma-separated arguments to filter options.")
async def wheel(ctx, args: str = None):
    """Spins a wheel with optional comma-separated arguments to filter options."""
    # Parse comma-separated arguments if provided
    filter_options = []
    if args:
        filter_options = [option.strip() for option in args.split(',')]
        await ctx.respond(f"🎯 Filtering wheel options to: {', '.join(filter_options)}")

    selected, gif_io, _ = generate_wheel_gif(ctx, filter_options)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=filter_options,
        title=f"🎉 The wheel landed on: {selected}!",
        description="wheel selection"
    )

bot.run(TOKEN)