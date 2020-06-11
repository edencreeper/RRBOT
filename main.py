import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '//')

#Once bot online print in terminal
@client.event
async def on_ready():
  print('Bot Online')


client.run('NzIwNzExMzAyMDE1ODc3MTUx.XuJ9ow.t3PMpCSBpazWNFbvJ9FVPc89qdo')