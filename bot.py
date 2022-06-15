import os
from pydoc import describe
from turtle import title
import discord
from discord.ext import commands

import platform
# Start
client = discord.Client()
bot = commands.Bot(command_prefix="!!", help_command=None)

# login vanity
@bot.event
async def on_ready():
    print("Logged as {0.user}".format(bot))
    print(platform.node() + " Joined as admin");

    # bot presence
    await bot.change_presence(activity=discord.Game(name="You Need to smiling :)"))

# command
# you should using prefix with @bot.command or using nonType Message as client.event
# im guide with prefix and nonType message
helpMessage = """
`help` - return the help message
`test` - new begining
`embed` - new as embed
`purge` - Purging channel {requirement : (amount)} - Permission = ManageMessages
`say` - Say All User Message
"""
@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="Pong ! :ping_pong:", description=f"{round(bot.latency * 1000)} Ms", color=discord.Colour.random())
    await ctx.send(embed=embed)
  
@bot.command()
async def test(ctx):
    await ctx.send(f"Hello {ctx.author.mention}") # Without embed

@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="This is the embed message", description="Any message has provided in here", color=discord.Colour.random())
    await ctx.send(embed=embed)

# bot list command / help function 

@bot.command()
async def help(ctx):
  embed = discord.Embed(title=f"{ctx.author} - Help Command", description="This is the available course :", color=discord.Colour.random())
  embed.add_field(name="Commands :", value=helpMessage)
  await ctx.send(embed=embed)

# say command by using args argument
@bot.command()
async def say(ctx, *, messages=None):
    if messages is not None:
        await ctx.send(f"{messages}")
        await ctx.message.delete()

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    await ctx.send(f"{ctx.author} Has purging this channel!")
    await ctx.channel.purge(limit=amount)
 
# if you dont have the permissions
@purge.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")
 

@bot.command()
async def magic_ball(ctx, *, messages=None):
    import random
    if messages is not None :
        answer = ["yes", "no", "not sure", "100% YESS", "Absolutely Not", "Ask me again"]
        embed = discord.Embed(title="Magic 8 Ball", description=f"""
You asked : `{messages}`
The Answer : `{random.choice(answer)}`
        """, color=discord.Colour.random())
        await ctx.send(embed=embed)
# connect your bot
bot.run("Your bot token")
