import discord
from discord.ext import commands
import typing
bot = commands
import random
from PIL import Image
import io

@bot.command()
async def say(ctx, color: typing.Optional[discord.Colour] = discord.Embed.Empty, *, message):
    """Sends a message as the bot"""
    await ctx.message.delete()
    embed = discord.Embed(description=message,colour=color)
    embed.set_author(name=str(ctx.author),icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, user: typing.Optional[discord.Member]):
    """Sends a user's avatar"""
    if user == None:
        user = ctx.author
    
    embed = discord.Embed(title=f"{str(user)}'s avatar",colour=0x7722ff)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def color(ctx, color: typing.Optional[discord.Color]):
    if color == None:
        color = discord.Color(random.randint(0,0xffffff))
    
    embed = discord.Embed(colour=color)
    embed.add_field(name="Hex",value=str(color),inline=False)
    embed.add_field(name="RGB",value=str(discord.Color.to_rgb(color)).replace("(","").replace(")",""),inline=False)
    embed.set_thumbnail(url="attachment://image.png")
    with io.BytesIO() as image_binary:
        Image.new("RGB",(256,256),discord.Color.to_rgb(color)).save(image_binary,"PNG")
        image_binary.seek(0)
        await ctx.send(embed=embed,file=discord.File(fp=image_binary, filename="image.png"))

def setup(client):
    client.add_command(say)
    client.add_command(avatar)
    client.add_command(color)