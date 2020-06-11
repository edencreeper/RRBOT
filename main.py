import discord
from discord.ext import commands
import os
client = commands.Bot(command_prefix = '//')

#Once bot online print in terminal
@client.event
async def on_ready():
  print('Bot Online')


client.run(token)