import discord
from discord.ext import commands
import typing
bot = commands
import asyncio
import subprocess

@bot.command()
async def playurl(ctx,url):
    voice_channel = ctx.author.voice.channel
    if voice_channel != None:
        await ctx.reply(f"Playing `{url}`")
        vc = await voice_channel.connect()
        if "youtube.com" in url or "youtu.be" in url:
            ytdlpopen = subprocess.Popen(["youtube-dl","--quiet","-o","-",url],stdout=subprocess.PIPE)
            vc.play(discord.FFmpegOpusAudio(ytdlpopen.stdout,pipe=True))
        else:
            vc.play(discord.FFmpegOpusAudio(url))
        while vc.is_playing():
            await asyncio.sleep(0.1)
        await vc.disconnect()

from youtube_search import YoutubeSearch
@bot.command()
async def play(ctx,*,query):
    search = YoutubeSearch(query,max_results=1).to_dict()[0]
    url = "https://youtube.com"+search["url_suffix"]
    voice_channel = ctx.author.voice.channel
    if voice_channel != None:
        ytdlpopen = subprocess.Popen(["youtube-dl","--quiet","--audio-format","flac","-o","-",url],stdout=subprocess.PIPE)
        try:
            vc = await voice_channel.connect()
        except:
            vc = ctx.guild.voice_client
        try:
            vc.play(discord.FFmpegOpusAudio(ytdlpopen.stdout,pipe=True))
            await ctx.reply(f"Playing `{search['title']}` by `{search['channel']}`")
        except discord.errors.ClientException:
            await ctx.send("Already playing a song!")
        while vc.is_playing():
            await asyncio.sleep(0.1)
        await vc.disconnect()

@bot.command()
async def leave(ctx):
    try:
        author_vc = ctx.author.voice.channel.id
    except:
        author_vc="Not In VC"
    try:
        bot_vc = ctx.guild.voice_client.channel.id
    except:
        bot_vc = "no"
    if author_vc == bot_vc:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.reply("you must be in the same vc as me!")

def setup(client):
    client.add_command(playurl)
    client.add_command(play)
    client.add_command(leave)