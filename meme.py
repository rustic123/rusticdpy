import discord
import json
import urllib
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print('Bot is online')

@bot.command()
async def meme(ctx):
  memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')

  memeData = json.load(memeAPI)

  memeUrl = memeData['url']
  memeName = memeData['title']


  embed = discord.Embed(title=memeName, colour=discord.Colour.orange())
  embed.set_image(url=memeUrl)
  await ctx.send(embed=embed)

bot.run('your token here')
