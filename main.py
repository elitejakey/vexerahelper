#IMPORTS
from discord.ext import commands
from discord.ext import tasks
import discord
import math
import asyncio
import secrets
import random
import datetime
import json
import platform
import aiohttp
import os


#SETTINGS

TOKEN = os.environ["DISCORD_TOKEN"]
bot = commands.Bot(command_prefix="%", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"vexera.io/docs"))
    print(f"Bot Online\n\nVexera Helper is in: {len(bot.guilds)} servers!")
#LOAD EXTENSIONS
bot.load_extension("cogs.snippets")
bot.load_extension("cogs.testslash")
bot.load_extension("cogs.errorhandler")
bot.load_extension("cogs.previewsnippets")

#BOT RUN
bot.run(TOKEN)