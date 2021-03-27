import discord
from discord.ext import commands
import typing
import random
from PIL import Image
import io
import os

bot = commands.Bot(command_prefix=["JAMB ","Jamb ","jamb "],description="Just Another Multipurpose Bot")

exts = os.listdir("extensions")
try:
    exts.remove("__pycache__")
except:
    pass

for ext in exts:
    bot.load_extension("extensions."+ext.replace(".py",""))

bot.run("TOKEN")
