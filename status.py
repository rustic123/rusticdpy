import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot is online!")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('With Mods'))

bot.run('your discord token here')
