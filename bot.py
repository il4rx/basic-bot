import os
import discord
from discord.ext import commands
import platform
import time, datetime
from time import sleep

intents = discord.Intents().all()
client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix="!!", help_command=None, intents=intents)

@bot.event
async def on_ready():
    print("Logged as {0.user}".format(bot))
    print(platform.node() + " Joined as admin");
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="Activity goes here"))
    
helpMessage = """
`help` - return the help message
`test` - new begining
`embed` - new as embed
`purge` - Purging channel {requirement : (amount)} - Permission = ManageMessages
`say` - Say All User Message
"""
@bot.command()
async def test(ctx):
    await ctx.send(f"Hello {ctx.author.mention}") # Without embed

@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="This is the embed message", description="Any message has provided in here", color=discord.Colour.random())
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title=f"{ctx.author} - Help Command", description="This is the available course :", color=discord.Colour.random())
  embed.add_field(name="Commands :", value=helpMessage)
  await ctx.send(embed=embed)

@bot.command()
async def say(ctx, messages):
    await ctx.send(f"{ctx.author.mention} has typing --> {messages}")
    await ctx.delete.message()


@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    await ctx.send(f"{ctx.author} Has purging this channel!")
    await ctx.channel.purge(limit=amount)
 
@purge.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

bot.run("Your bot token")
