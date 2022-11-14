import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print('Bot is online')

@bot.command(aliases=['membercount'])
async def members(ctx):
  await ctx.send(f"Members: ***{ctx.guild.member_count)***")

bot.run('your token here')
