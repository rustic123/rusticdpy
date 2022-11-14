import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())
bot.remove_command("help")

@bot.command()
async def help(ctx):
  em = discord.Embed(title='Drome Help Menu',description='Join our discord for support!', color=discord.Color.yellow())
  em.add_field(name='Moderation', value='`ban`, `kick`, `unban`')
  em.add_field(name='Fun', value='`8ball`, `motivate`, `hello`, `meme`')
  em.add_field(name='Information', value='`serverinfo`')
  em.add_field(name='Support', value='`discord`, `support`, `invite` ')
  await ctx.send(embed=em)
 
bot.run('your discord token here')
