import discord
from discord.ext import commands
import logging
import os
import asyncio
from dotenv import load_dotenv
from wheel import generate_wheel_gif, spin_wheel_and_show_result

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

# Logging setup
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Game data
boards1 = {
    1: "DK's Jungle Adventure",
    2: "Peach's Birthday Cake",
    3: "Yoshi's Tropical Island",
    4: "Wario's Battle Canyon",
    5: "Luigi's Engine Room",
    6: "Mario's Rainbow Castle",
    7: "Bowser's Magma Mountain",
    8: "Eternal Star"
}

boards1IMG = {
    1: "assets/DK's Jungle Adventure.png",
    2: "assets/Peach's Birthday Cake.png",
    3: "assets/Yoshi's Tropical Island.png",
    4: "assets/Wario's Battle Canyon.png",
    5: "assets/Luigi's Engine Room.png",
    6: "assets/Mario's Rainbow Castle.png",
    7: "assets/Bowser's Magma Mountain.png",
    8: "assets/Eternal Star.png"
}

boards2 = {
    1: "Pirate Land",
    2: "Western Land",
    3: "Space Land",
    4: "Mystery Land",
    5: "Horror Land",
    6: "Bowser Land"
}

boards2IMG = {
    1: "assets/Pirate Land.png",
    2: "assets/Western Land.png",
    3: "assets/Space Land.png",
    4: "assets/Mystery Land.png",
    5: "assets/Horror Land.png",
    6: "assets/Bowser Land.png"
}

boards3 = {
    1: "Chilly Waters",
    2: "Deep Bloober Sea",
    3: "Spiny Desert",
    4: "Woody Woods",
    5: "Creepy Cavern",
    6: "Waluigi's Island"
}

boards3IMG = {
    1: "assets/Chilly Waters.png",
    2: "assets/Deep Bloober Sea.png",
    3: "assets/Spiny Desert.png",
    4: "assets/Woody Woods.png",
    5: "assets/Creepy Cavern.png",
    6: "assets/Waluigi's Island.png"
}

boards4 = {
    1: "Toad's Midway Madness",
    2: "Shy Guy's Jungle Jam",
    3: "Goomba's Greedy Gala",
    4: "Boo's Haunted Bash",
    5: "Koopa's Seaside Soiree",
    6: "Bowser's Gnarly Party"
}

boards4IMG = {
    1: "assets/Toad's Midway Madness.png",
    2: "assets/Shy Guy's Jungle Jam.png",
    3: "assets/Goomba's Greedy Gala.png",
    4: "assets/Boo's Haunted Bash.png",
    5: "assets/Koopa's Seaside Soiree.png",
    6: "assets/Bowser's Gnarly Party.png"
}

boards5 = {
    1: "Toy Dream",
    2: "Rainbow Dream",
    3: "Pirate Dream",
    4: "Undersea Dream",
    5: "Future Dream",
    6: "Sweet Dream",
    7: "Bowser's Nightmare"
}

boards5IMG = {
    1: "assets/Toy Dream.png",
    2: "assets/Rainbow Dream.png",
    3: "assets/Pirate Dream.png",
    4: "assets/Undersea Dream.png",
    5: "assets/Future Dream.png",
    6: "assets/Sweet Dream.png",
    7: "assets/Bowser's Nightmare.png"
}

boards6 = {
    1: "Towering Treetop",
    2: "E.Gadd's Garage",
    3: "Faire Square",
    4: "Snowflake Lake",
    5: "Castaway Bay",
    6: "Clockwork Castle"
}

boards6IMG = {
    1: "assets/Towering Treetop.png",
    2: "assets/E.Gadd's Garage.png",
    3: "assets/Faire Square.png",
    4: "assets/Snowflake Lake.png",
    5: "assets/Castaway Bay.png",
    6: "assets/Clockwork Castle.png"
}

boards7 = {
    1: "Grand Canal",
    2: "Pagoda Peak",
    3: "Pyramid Park",
    4: "Neon Heights",
    5: "Windmillville",
    6: "Bowser's Enchanted Inferno"
}

boards7IMG = {
    1: "assets/Grand Canal.png",
    2: "assets/Pagoda Peak.png",
    3: "assets/Pyramid Park.png",
    4: "assets/Neon Heights.png",
    5: "assets/Windmillville.png",
    6: "assets/Bowser's Enchanted Inferno.png"
}

boards8 = {
    1: "DK's Treetop Temple",
    2: "Goomba's Booty Boardwalk",
    3: "King Boo's Haunted Hideaway",
    4: "Shy Guy's Perplex Express",
    5: "Koopa's Tycoon Town",
    6: "Bowser's Warped Orbit"
}

boards8IMG = {
    1: "assets/DK's Treetop Temple.png",
    2: "assets/Goomba's Booty Boardwalk.png",
    3: "assets/King Boo's Haunted Hideaway.png",
    4: "assets/Shy Guy's Perplex Express.png",
    5: "assets/Koopa's Tycoon Town.png",
    6: "assets/Bowser's Warped Orbit.png"
}

mayhemgamemode = {
    1: "Mario Party Mayhem: Classic",
    2: "Mario Party Mayhem: Modern",
    3: "Mario Party Mayhem: Magic Conch",
    4: "Mario Party Mayhem: Mayhem Says",
    5: "Mario Party Mayhem: Raiders Wrath",
    6: "Mario Party Mayhem: Inversal Reversal"
}

normalgamemode = {
    1: "Mario Party: Magic Conch",
    2: "Mario Party: Simon Says",
    3: "Mario Party: Raiders Wrath",
    4: "Mario Party: Inversal Reversal"
}

gamesIMG = {
    1: "assets/MP1.png",
    2: "assets/MP2.png",
    3: "assets/MP3.png",
    4: "assets/MP4.png",
    5: "assets/MP5.png",
    6: "assets/MP6.png",
    7: "assets/MP7.png",
    8: "assets/MP8.png"
}

COMMANDS_LIST = [
    "$board1", "$board2", "$board3", "$board4", "$board5", "$board6", "$board7", "$board8",
    "$bonusstars", "$commands", "$duels", "$gentlemans", "$pickgame", "$pickgcwii", 
    "$pickMPmode", "$pickMP4mode", "$pickn64", "$pickmayhemgamemode", "$picknormalgamemode", "$wheel"
]

def get_board_key_by_value(board_dict, value):
    """Get the key for a given board value."""
    for key, val in board_dict.items():
        if val == value:
            return key
    return None

# Bot events
@bot.event
async def on_ready():
    print(f'Now Running {bot.user}!')

# Board selection commands
@bot.command(name="board1")
async def board1(ctx):
    """Selects a random Mario Party 1 board using the wheel."""
    selected, gif_io, _ = generate_wheel_gif(ctx, list(boards1.values()))
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(boards1.values()),
        title="🎯 Mario Party 1 Board Selected!",
        description="MP1 board",
        image_path=boards1IMG[get_board_key_by_value(boards1, selected)],
        filename=f"{selected}.png"
    )

@bot.command(name="board2")
async def board2(ctx):
    """Selects a random Mario Party 2 board using the wheel."""
    selected, gif_io, _ = generate_wheel_gif(ctx, list(boards2.values()))
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(boards2.values()),
        title="🎯 Mario Party 2 Board Selected!",
        description="MP2 board",
        image_path=boards2IMG[get_board_key_by_value(boards2, selected)],
        filename=f"{selected}.png"
    )

@bot.command(name="board3")
async def board3(ctx):
    """Selects a random Mario Party 3 board using the wheel."""
    selected, gif_io, _ = generate_wheel_gif(ctx, list(boards3.values()))
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(boards3.values()),
        title="🎯 Mario Party 3 Board Selected!",
        description="MP3 board",
        image_path=boards3IMG[get_board_key_by_value(boards3, selected)],
        filename=f"{selected}.png"
    )

@bot.command(name="board4")
async def board4(ctx):
    """Selects a random Mario Party 4 board using the wheel."""
    selected, gif_io, _ = generate_wheel_gif(ctx, list(boards4.values()))
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(boards4.values()),
        title="🎯 Mario Party 4 Board Selected!",
        description="MP4 board",
        image_path=boards4IMG[get_board_key_by_value(boards4, selected)],
        filename=f"{selected}.png"
    )

@bot.command(name="board5")
async def board5(ctx):
    """Selects a random Mario Party 5 board using the wheel."""
    selected, gif_io, _ = generate_wheel_gif(ctx, list(boards5.values()))
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(boards5.values()),
        title="🎯 Mario Party 5 Board Selected!",
        description="MP5 board",
        image_path=boards5IMG[get_board_key_by_value(boards5, selected)],
        filename=f"{selected}.png"
    )

@bot.command(name="board6")
async def board6(ctx):
    """Selects a random Mario Party 6 board using the wheel."""
    selected, gif_io, _ = generate_wheel_gif(ctx, list(boards6.values()))
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(boards6.values()),
        title="🎯 Mario Party 6 Board Selected!",
        description="MP6 board",
        image_path=boards6IMG[get_board_key_by_value(boards6, selected)],
        filename=f"{selected}.png"
    )

@bot.command(name="board7")
async def board7(ctx):
    """Selects a random Mario Party 7 board using the wheel."""
    selected, gif_io, _ = generate_wheel_gif(ctx, list(boards7.values()))
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(boards7.values()),
        title="🎯 Mario Party 7 Board Selected!",
        description="MP7 board",
        image_path=boards7IMG[get_board_key_by_value(boards7, selected)],
        filename=f"{selected}.png"
    )

@bot.command(name="board8")
async def board8(ctx):
    """Selects a random Mario Party 8 board using the wheel."""
    selected, gif_io, _ = generate_wheel_gif(ctx, list(boards8.values()))
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(boards8.values()),
        title="🎯 Mario Party 8 Board Selected!",
        description="MP8 board",
        image_path=boards8IMG[get_board_key_by_value(boards8, selected)],
        filename=f"{selected}.png"
    )

# Game selection commands
@bot.command(name="pickgame")
async def pickgame(ctx):
    """Selects a random Mario Party game using the wheel."""
    game_names = [f"Mario Party {i}" for i in range(1, 9)]
    selected, gif_io, _ = generate_wheel_gif(ctx, game_names)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=game_names,
        title="🎮 Mario Party Game Selected!",
        description="Mario Party game",
        image_path=gamesIMG[int(selected.split()[-1])],
        filename=f"MP{int(selected.split()[-1])}.png"
    )

@bot.command(name="pickgcwii")
async def pickgcwii(ctx):
    """Selects a random GameCube/Wii Mario Party game using the wheel."""
    game_names = [f"Mario Party {i}" for i in range(4, 9)]
    selected, gif_io, _ = generate_wheel_gif(ctx, game_names)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=game_names,
        title="🎮 GC/Wii Mario Party Game Selected!",
        description="GC/Wii Mario Party game",
        image_path=gamesIMG[int(selected.split()[-1])],
        filename=f"MP{int(selected.split()[-1])}.png"
    )

@bot.command(name="pickn64")
async def pickn64(ctx):
    """Selects a random N64 Mario Party game using the wheel."""
    game_names = [f"Mario Party {i}" for i in range(1, 4)]
    selected, gif_io, _ = generate_wheel_gif(ctx, game_names)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=game_names,
        title="🎮 N64 Mario Party Game Selected!",
        description="N64 Mario Party game",
        image_path=gamesIMG[int(selected.split()[-1])],
        filename=f"MP{int(selected.split()[-1])}.png"
    )

# Game mode commands
@bot.command(name="picknormalgamemode")
async def picknormalgamemode(ctx):
    """Selects a random normal game mode using the wheel."""
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(normalgamemode.values()),
        title="🎯 Normal Game Mode Selected!",
        description="normal game mode"
    )

@bot.command(name="pickmayhemgamemode")
async def pickmayhemgamemode(ctx):
    """Selects a random mayhem game mode using the wheel."""
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=list(mayhemgamemode.values()),
        title="🎯 Mayhem Game Mode Selected!",
        description="mayhem game mode"
    )

@bot.command(name="pickMP4mode")
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

@bot.command(name="pickMPmode")
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
@bot.command(name="bonusstars")
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

@bot.command(name="duels")
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

@bot.command(name="gentlemans")
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
@bot.command(name="commands")
async def commands(ctx):
    """Shows the list of available commands."""
    commands_string = "\n".join(COMMANDS_LIST)
    await ctx.send("## Here's The List of Commands!")
    await ctx.send(commands_string)

@bot.command(name='wheel')
async def wheel(ctx, *, args=None):
    """Spins a wheel with optional comma-separated arguments to filter options."""
    # Parse comma-separated arguments if provided
    filter_options = []
    if args:
        filter_options = [option.strip() for option in args.split(',')]
        await ctx.send(f"🎯 Filtering wheel options to: {', '.join(filter_options)}")

    selected, gif_io, _ = generate_wheel_gif(ctx, filter_options)
    await spin_wheel_and_show_result(
        ctx=ctx,
        options=filter_options,
        title=f"🎉 The wheel landed on: {selected}!",
        description="wheel selection"
    )

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)