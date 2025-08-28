import discord
from discord.ext import commands

import logging

import random

import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

commandsList = ["$board1", "$board2", "$board3", "$board4", "$board5", "$board6", "$board7", "$board8", "$bonusstars", "$commands", "$duels", "$gentlemans", "$pickgame", "$pickgcwii", "$pickMPmode", "$pickMP4mode", "$pickn64", "$pickmayhemgamemode", "$picknormalgamemode"]

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
    7: "assets/Bowser's Nightmare.png",
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

@bot.event
async def on_ready():
    print(f'Now Running {bot.user}!')

@bot.command(name="board1")
async def board1(ctx):
    randint = random.randint(1,8)
    selection = boards1[randint]
    file_path = boards1IMG[randint]
    
    if randint == 1:
        file = discord.File(file_path, filename="DK's Jungle Adventure.png")
        await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
    elif randint == 2:
        file = discord.File(file_path, filename="Peach's Birthday Cake.png")
        await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
    elif randint == 3:
        file = discord.File(file_path, filename="Yoshi's Tropical Island.png")
        await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
    elif randint == 4:
        file = discord.File(file_path, filename="Wario's Battle Canyon.png")
        await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
    elif randint == 5:
        file = discord.File(file_path, filename="Luigi's Engine Room.png")
        await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
    elif randint == 6:
        file = discord.File(file_path, filename="Mario's Rainbow Castle.png")
        await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
    elif randint == 7:
        file = discord.File(file_path, filename="Bowser's Magma Mountain.png")
        await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
    elif randint == 8:
        file = discord.File(file_path, filename="Eternal Star.png")
        await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)

@bot.command(name="board2")
async def board2(ctx):
    randint = random.randint(1,6)
    selection = boards2[randint]
    file_path = boards2IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="Pirate Land.png")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="Western Land.png")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="Space Land.png")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="Mystery Land.png")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="Horror Land.png")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="Bowser Land.png")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)

@bot.command(name="board3")
async def board3(ctx):
    randint = random.randint(1,6)
    selection = boards3[randint]
    file_path = boards3IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="Chilly Waters.png")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="Deep Bloober Sea.png")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="Spiny Desert.png")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="Woody Woods.png")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="Creepy Cavern.png")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="Waluigi's Island.png")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)

@bot.command(name="board4")
async def board4(ctx):
    randint = random.randint(1,6)
    selection = boards4[randint]
    file_path = boards4IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="Toad's Midway Madness.png")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="Goomba's Greedy Gala.png")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="Shy Guy's Jungle Jam.png")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="Boo's Haunted Bash.png")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="Koopa's Seaside Soiree.png")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="Bowser's Gnarly Party.png")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)

@bot.command(name="board5")
async def board5(ctx):
    randint = random.randint(1,7)
    selection = boards5[randint]
    file_path = boards5IMG[randint]

    match randint:
        case 1:
            file = discord.File(file_path, filename="Toy Dream.png")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="Rainbow Dream.png")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="Pirate Dream.png")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="Undersea Dream.png")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="Future Dream.png")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="Sweet Dream.png")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 7:
            file = discord.File(file_path, filename="Bowser's Nightmare.png")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)

@bot.command(name="board6")
async def board6(ctx):
    randint = random.randint(1,6)
    selection = boards6[randint]
    file_path = boards6IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="Towering Treetop.png")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="E.Gadd's Garage.png")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="Faire Square.png")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="Snowflake Lake.png")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="Castaway Bay.png")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="Clockwork Castle.png")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)

@bot.command(name="board7")
async def board7(ctx):
    randint = random.randint(1,6)
    selection = boards7[randint]
    file_path = boards7IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="Grand Canal.png")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="Pagoda Peak.png")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="Pyramid Park.png")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="Neon Heights.png")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="Windmillville.png")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="Bowser's Enchanted Inferno.png")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)

@bot.command(name="board8")
async def board8(ctx):
    randint = random.randint(1,6)
    selection = boards8[randint]
    file_path = boards8IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="DK's Treetop Temple.png")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="Goomba's Booty Boardwalk.png")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="King Boo's Haunted Hideaway.png")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="Shy Guy's Perplex Express.png")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="Koopa's Tycoon Town.png")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="Bowser's Warped Orbit.png")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)


@bot.command(name="pickgame")
async def pickgame(ctx):
    randint = random.randint(1,8)
    file_path = gamesIMG[randint]

    if randint == 1:
        file = discord.File(file_path, filename="MP1.png")
        await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
    elif randint == 2:
        file = discord.File(file_path, filename="MP2.png")
        await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
    elif randint == 3:
        file = discord.File(file_path, filename="MP3.png")
        await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
    elif randint == 4:
        file = discord.File(file_path, filename="MP4.png")
        await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
    elif randint == 5:
        file = discord.File(file_path, filename="MP5.png")
        await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
    elif randint == 6:
        file = discord.File(file_path, filename="MP6.png")
        await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
    elif randint == 7:
        file = discord.File(file_path, filename="MP7.png")
        await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
    elif randint == 8:
        file = discord.File(file_path, filename="MP8.png")
        await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)

@bot.command(name="pickgcwii")
async def pickgcwii(ctx):
    randint = random.randint(4,8)
    file_path = gamesIMG[randint]

    match randint:
        case 4:
            file = discord.File(file_path, filename="MP4.png")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 5:
            file = discord.File(file_path, filename="MP5.png")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 6:
            file = discord.File(file_path, filename="MP6.png")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 7:
            file = discord.File(file_path, filename="MP7.png")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 8:
            file = discord.File(file_path, filename="MP8.png")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)

@bot.command(name="pickn64")
async def pickn64(ctx):
    randint = random.randint(1,3)
    file_path = gamesIMG[randint]

    match randint:
        case 1:
            file = discord.File(file_path, filename="MP1.png")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 2:
            file = discord.File(file_path, filename="MP2.png")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 3:
            file = discord.File(file_path, filename="MP3.png")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)

@bot.command(name="picknormalgamemode")
async def picknormalgamemode(ctx):
    randint = random.randint(1,3)

    if randint == 1:
        selection = normalgamemode[1]
        await ctx.send("## The Selected Normal Game Mode is... " + selection)
    elif randint == 2:
        selection = normalgamemode[2]
        await ctx.send("## The Selected Normal Game Mode is... " + selection)
    else:
        selection = normalgamemode[3]
        await ctx.send("## The Selected Normal Game Mode is... " + selection)

@bot.command(name="pickmayhemgamemode")
async def pickmayhemgamemode(ctx):
    randint = random.randint(1,6)
    if randint == 1:    
        selection = mayhemgamemode[1]
        await ctx.send("## The Selected Mayhem Game Mode is... " + selection)
    elif randint == 2:
        selection = mayhemgamemode[2]
        await ctx.send("## The Selected Mayhem Game Mode is... " + selection)
    elif randint == 3:
        selection = mayhemgamemode[3]
        await ctx.send("## The Selected Mayhem Game Mode is... " + selection)
    elif randint == 4:
        selection = mayhemgamemode[4]
        await ctx.send("## The Selected Mayhem Game Mode is... " + selection)
    elif randint == 5:
        selection = mayhemgamemode[5]
        await ctx.send("## The Selected Mayhem Game Mode is... " + selection)
    else:
        selection = mayhemgamemode[6]
        await ctx.send("## The Selected Mayhem Game Mode is... " + selection)

@bot.command(name="pickMP4mode")
async def pickMP4mode(ctx):
    randint = random.randint(1,2)

    if randint == 1:
        
        await ctx.send("## The Selected Mario Party 4 Version is... Vanilla")
    elif randint == 2:
        await ctx.send("## The Selected Mario Party 4 Version is... DX")

@bot.command(name="bonusstars")
async def bstars(ctx):
    randint = random.randint(1,3)

    if randint == 1:
        
        await ctx.send("## Bonus Stars Will Be... Off")
    elif randint == 2:
        await ctx.send("## Bonus Stars Will Be... On")
    else:
        await ctx.send("## Bonus Stars Will Be... Ztars")

@bot.command(name="duels")
async def duels(ctx):
    randint = random.randint(1,3)

    if randint == 1:
        await ctx.send("## Same Space Duels is set to... Always")
    elif randint == 2:
        await ctx.send("## Same Space Duels is set to... Vanilla")
    else:
        await ctx.send("## Same Space Duels is set to... Never")

@bot.command(name="gentlemans")
async def gentlemans(ctx):
    randint = random.randint(1,2)

    if randint == 1:
        await ctx.send("## Gentleman's Rule is set to... On")
    else:
        await ctx.send("## Gentleman's Rule is set to... Off")

@bot.command(name="pickMPmode")
async def pickMPmode(ctx):
    randint = random.randint(1,2)

    if randint == 1:
        await ctx.send("## The Game Mode Selected is... Vanilla")
    else:
        await ctx.send("## The Game Mode Selected is... Mayhem")

@bot.command(name="commands")
async def commands(ctx):
    commandsString = ""

    for _command in commandsList:
        commandsString += _command
        commandsString += "\n"

    await ctx.send("## Here's The List of Commands!")
    await ctx.send(commandsString)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)