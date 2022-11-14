import discord
import asyncio
import os


intents = discord.Intents.all()
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print("Bot is online")

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(123456789012345678)
    print(f"{member} has joined!")
    await welcome_channel.send(f"Hey {member.mention}, welcome to the server!")
    try:
        await member.send(f"Hey {member.display_name}, Thank you for joining the server :heart:")
    except:
        await welcome_channel.send(f"{member.mention} I can't dm you, but thank you for joining!")
   
client.run('your token here')
