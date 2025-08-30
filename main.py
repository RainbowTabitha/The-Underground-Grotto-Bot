import discord
import logging
import os
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
    logger.info(f"Joined guild: {guild.name} (ID: {guild.id})")
    print(f"🎉 Joined new guild: {guild.name}")


@bot.event
async def on_guild_remove(guild):
    logger.info(f"Left guild: {guild.name} (ID: {guild.id})")
    print(f"👋 Left guild: {guild.name}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ApplicationCommandInvokeError):
        logger.error(f"Command error in {ctx.command}: {error.original}")
        await ctx.respond(f"❌ An error occurred: {str(error.original)}", ephemeral=True)
    else:
        logger.error(f"Unexpected error: {error}")
        await ctx.respond("❌ An unexpected error occurred.", ephemeral=True)


# Board selection commands
@bot.slash_command(name="board1", description="Random Mario Party 1 board")
async def board1(ctx):
    boards = [
        "DK's Jungle Adventure", "Peach's Birthday Cake", "Yoshi's Tropical Island",
        "Wario's Battle Canyon", "Luigi's Engine Room", "Mario's Rainbow Castle",
        "Bowser's Magma Mountain", "Eternal Star"
    ]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards)
    await spin_wheel_and_show_result(ctx, boards, "🎯 Mario Party 1 Board Selected!", "MP1 board",
                                     f"assets/{selected}.png", f"{selected}.png")


@bot.slash_command(name="board2", description="Random Mario Party 2 board")
async def board2(ctx):
    boards = ["Pirate Land", "Western Land", "Space Land", "Mystery Land", "Horror Land", "Bowser Land"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards)
    await spin_wheel_and_show_result(ctx, boards, "🎯 Mario Party 2 Board Selected!", "MP2 board",
                                     f"assets/{selected}.png", f"{selected}.png")


@bot.slash_command(name="board3", description="Random Mario Party 3 board")
async def board3(ctx):
    boards = ["Chilly Waters", "Deep Bloober Sea", "Spiny Desert", "Woody Woods", "Creepy Cavern", "Waluigi's Island"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards)
    await spin_wheel_and_show_result(ctx, boards, "🎯 Mario Party 3 Board Selected!", "MP3 board",
                                     f"assets/{selected}.png", f"{selected}.png")


@bot.slash_command(name="board4", description="Random Mario Party 4 board")
async def board4(ctx):
    boards = ["Toad's Midway Madness", "Shy Guy's Jungle Jam", "Goomba's Greedy Gala",
              "Boo's Haunted Bash", "Koopa's Seaside Soiree", "Bowser's Gnarly Party"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards)
    await spin_wheel_and_show_result(ctx, boards, "🎯 Mario Party 4 Board Selected!", "MP4 board",
                                     f"assets/{selected}.png", f"{selected}.png")


@bot.slash_command(name="board5", description="Random Mario Party 5 board")
async def board5(ctx):
    boards = ["Toy Dream", "Rainbow Dream", "Pirate Dream", "Undersea Dream", "Future Dream", "Sweet Dream", "Bowser's Nightmare"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards)
    await spin_wheel_and_show_result(ctx, boards, "🎯 Mario Party 5 Board Selected!", "MP5 board",
                                     f"assets/{selected}.png", f"{selected}.png")


@bot.slash_command(name="board6", description="Random Mario Party 6 board")
async def board6(ctx):
    boards = ["Towering Treetop", "E.Gadd's Garage", "Faire Square", "Snowflake Lake", "Castaway Bay", "Clockwork Castle"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards)
    await spin_wheel_and_show_result(ctx, boards, "🎯 Mario Party 6 Board Selected!", "MP6 board",
                                     f"assets/{selected}.png", f"{selected}.png")


@bot.slash_command(name="board7", description="Random Mario Party 7 board")
async def board7(ctx):
    boards = ["Grand Canal", "Pagoda Peak", "Pyramid Park", "Neon Heights", "Windmillville", "Bowser's Enchanted Inferno"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards)
    await spin_wheel_and_show_result(ctx, boards, "🎯 Mario Party 7 Board Selected!", "MP7 board",
                                     f"assets/{selected}.png", f"{selected}.png")


@bot.slash_command(name="board8", description="Random Mario Party 8 board")
async def board8(ctx):
    boards = ["DK's Treetop Temple", "Goomba's Booty Boardwalk", "King Boo's Haunted Hideaway",
              "Shy Guy's Perplex Express", "Koopa's Tycoon Town", "Bowser's Warped Orbit"]
    selected, gif_io, _ = generate_wheel_gif(ctx, boards)
    await spin_wheel_and_show_result(ctx, boards, "🎯 Mario Party 8 Board Selected!", "MP8 board",
                                     f"assets/{selected}.png", f"{selected}.png")


# Game selection commands
@bot.slash_command(name="pickgame", description="Random Mario Party game")
async def pickgame(ctx):
    games = [f"Mario Party {i}" for i in range(1, 9)]
    selected, gif_io, _ = generate_wheel_gif(ctx, games)
    await spin_wheel_and_show_result(ctx, games, "🎮 Mario Party Game Selected!", "Mario Party game",
                                     f"assets/MP{int(selected.split()[-1])}.png", f"MP{int(selected.split()[-1])}.png")


@bot.slash_command(name="pickgcwii", description="Random GC/Wii Mario Party game")
async def pickgcwii(ctx):
    games = [f"Mario Party {i}" for i in range(4, 9)]
    selected, gif_io, _ = generate_wheel_gif(ctx, games)
    await spin_wheel_and_show_result(ctx, games, "🎮 GC/Wii Mario Party Game Selected!", "GC/Wii Mario Party game",
                                     f"assets/MP{int(selected.split()[-1])}.png", f"MP{int(selected.split()[-1])}.png")


@bot.slash_command(name="pickn64", description="Random N64 Mario Party game")
async def pickn64(ctx):
    games = [f"Mario Party {i}" for i in range(1, 4)]
    selected, gif_io, _ = generate_wheel_gif(ctx, games)
    await spin_wheel_and_show_result(ctx, games, "🎮 N64 Mario Party Game Selected!", "N64 Mario Party game",
                                     f"assets/MP{int(selected.split()[-1])}.png", f"MP{int(selected.split()[-1])}.png")


# Game mode commands
@bot.slash_command(name="picknormalgamemode", description="Random normal game mode")
async def picknormalgamemode(ctx):
    modes = ["Mario Party: Magic Conch", "Mario Party: Simon Says", "Mario Party: Raiders Wrath", "Mario Party: Inversal Reversal"]
    selected, gif_io, _ = generate_wheel_gif(ctx, modes)
    await spin_wheel_and_show_result(ctx, modes, "🎯 Normal Game Mode Selected!", "normal game mode")


@bot.slash_command(name="pickmayhemgamemode", description="Random mayhem game mode")
async def pickmayhemgamemode(ctx):
    modes = [
        "Mario Party Mayhem: Classic", "Mario Party Mayhem: Modern", "Mario Party Mayhem: Magic Conch",
        "Mario Party Mayhem: Mayhem Says", "Mario Party Mayhem: Raiders Wrath", "Mario Party Mayhem: Inversal Reversal"
    ]
    selected, gif_io, _ = generate_wheel_gif(ctx, modes)
    await spin_wheel_and_show_result(ctx, modes, "🎯 Mayhem Game Mode Selected!", "mayhem game mode")


@bot.slash_command(name="pickmp4mode", description="Random Mario Party 4 version")
async def pickMP4mode(ctx):
    modes = ["Vanilla", "DX"]
    selected, gif_io, _ = generate_wheel_gif(ctx, modes)
    await spin_wheel_and_show_result(ctx, modes, "🎯 Mario Party 4 Version Selected!", "MP4 version")


@bot.slash_command(name="pickmpmode", description="Random Mario Party mode")
async def pickMPmode(ctx):
    modes = ["Vanilla", "Mayhem"]
    selected, gif_io, _ = generate_wheel_gif(ctx, modes)
    await spin_wheel_and_show_result(ctx, modes, "🎮 Mario Party Mode Selected!", "Mario Party mode")


# Settings commands
@bot.slash_command(name="bonusstars", description="Random bonus stars setting")
async def bstars(ctx):
    options = ["Off", "On", "Ztars"]
    selected, gif_io, _ = generate_wheel_gif(ctx, options)
    await spin_wheel_and_show_result(ctx, options, "⭐ Bonus Stars Setting Selected!", "bonus stars setting")


@bot.slash_command(name="duels", description="Random duels setting")
async def duels(ctx):
    options = ["Always", "Vanilla", "Never"]
    selected, gif_io, _ = generate_wheel_gif(ctx, options)
    await spin_wheel_and_show_result(ctx, options, "⚔️ Same Space Duels Setting Selected!", "duels setting")


@bot.slash_command(name="gentlemans", description="Random gentleman's rule setting")
async def gentlemans(ctx):
    options = ["On", "Off"]
    selected, gif_io, _ = generate_wheel_gif(ctx, options)
    await spin_wheel_and_show_result(ctx, options, "🎩 Gentleman's Rule Setting Selected!", "gentleman's rule setting")


# Utility commands
@bot.slash_command(name="commands", description="Shows available commands")
async def commands(ctx):
    commands_string = "\n".join(get_commands_list())
    await ctx.respond("## Here's The List of Commands!")
    await ctx.respond(commands_string)


@bot.slash_command(name='wheel', description="Spin a wheel with optional args")
async def wheel(ctx, args: str = None):
    filter_options = []
    if args:
        filter_options = [option.strip() for option in args.split(',')]
        await ctx.respond(f"🎯 Filtering wheel options to: {', '.join(filter_options)}")

    selected, gif_io, _ = generate_wheel_gif(ctx, filter_options)
    await spin_wheel_and_show_result(ctx, filter_options, f"🎉 The wheel landed on: {selected}!", "wheel selection")


bot.run(TOKEN)
