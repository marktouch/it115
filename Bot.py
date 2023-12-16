
import discord
import os
from ec2_metadata import ec2_metadata

bot = discord.Bot()
TOKEN = str(os.getenv("discordBot"))

async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))

async def response(message):
  userInput = str(message.content).lower()

  match userInput:
    case "hello world":
      await message.send("hello "+str(message.author)+" EC2 Data: " + ec2_metadata.region)

    case "hello":
      await message.send("hello world")

    case "ping":
      await message.send("pong")

    case "Tell me about my server!":
      await message.send("IP Address: "+ec2_metadata.public_ipv4+" Region: "+ec2_metadata.region+" Availability Zone: "+ec2_metadata.availability_zone)

    case _:
      await message.send("owo")

bot.run(TOKEN)

"""
import discord
from discord.ext import commands
from discord.ext.commands.bot import Bot
from dotenv import load_dotenv
import os

load_dotenv(".env")
TOKEN = os.getenv("discordBot")

bot = commands.Bot(command_prefix="!")

@bot.command(name="ping")
async def pong(ctx):
    await ctx.send("pong")

bot.run(TOKEN)
"""
