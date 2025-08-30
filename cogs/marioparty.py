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

    async def spin_board_wheel(self, ctx, boardList, game_name):
        """Helper function to spin the wheel for any Mario Party game."""
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