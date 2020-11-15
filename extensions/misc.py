from discord.ext import commands as bot
import random

@bot.command()
async def joke(ctx):
    await ctx.send(random.choice(["no joke 4 u","so uhh, i went to the store to buy jokes, and they had ran out! can you believe it?!?","uhh... where are the jokes???"]))

def setup(botto):
    botto.add_command(joke)