import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print('Bot is online')
 
@bot.command()
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)

bot.run('your discord token here')
