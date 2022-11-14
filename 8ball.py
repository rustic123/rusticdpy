import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print('Bot is online')

@bot.command(aliases=['8ball'])
async def eightball(ctx, *, question):
  responses = ['Yes', 'No']

  await ctx.send(f":8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}")

bot.run('your discord token here')
