import discord
from discord.ext import commands
from discord.ext.commands.bot import Bot
from dotenv import load_dotenv
import os

load_dotenv('.env')
TOKEN = os.getenv("AWS_WS")
bot = commands.Bot(command_prefix="!")
@bot.command(name='ping')
async def pong(ctx):
  await ctx.send("pong")

bot.run(TOKEN)
