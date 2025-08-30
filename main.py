#***************************************************************************#
# Underground Grotto
#***************************************************************************#

import os
import platform
import discord

from cogs.base import Base
from cogs.fun import Fun 
from cogs.leveling import Leveling
from cogs.birthday import Birthday
from cogs.quotes import Quotes 
from cogs.marioparty import MarioParty

from discord.ext import tasks
from discord.ext import commands

#Intents
intents = discord.Intents.all()

#Define Client
bot = commands.Bot(command_prefix=commands.when_mentioned_or("/"), intents=intents, activity=discord.Game(name='Mario Party Mayhem'))

@bot.event
async def on_ready():
  memberCount = len(set(bot.get_all_members()))
  serverCount = len(bot.guilds)
  

  print("                                                                ")
  print("################################################################") 
  print(f"{bot.user.name}                                                ")
  print("################################################################") 
  print("Running as: " + bot.user.name + "#" + bot.user.discriminator)
  print(f'With Client ID: {bot.user.id}')
  print("\nBuilt With:")
  print("Python " + platform.python_version())
  print("Py-Cord " + discord.__version__)


#Boot Cogs
bot.add_cog(Base(bot))
bot.add_cog(Fun(bot))
bot.add_cog(Leveling(bot))
bot.add_cog(Birthday(bot))
bot.add_cog(Quotes(bot))
bot.add_cog(MarioParty(bot))

#Run Bot
TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN)