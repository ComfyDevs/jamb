from discord.ext import commands as bot

@bot.command()
async def help(ctx):
    await ctx.send("Command List:\n    help: show this message\n    joke: tells you a joke")

def setup(botto):
    botto.add_command(help)