import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print('Bot is online')

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = "member")
    await member.add_roles(role)

bot.run("your discord token here")
