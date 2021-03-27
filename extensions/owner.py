import discord
from discord.ext import commands
import typing
bot = commands

@bot.command(name="eval")
@commands.is_owner()
async def _eval(ctx, *, code):
    env = {
        "ctx": ctx,
        "discord": discord,
        "commands": commands,
        "bot": ctx.bot,
        "__import__": __import__
    }

    splitcode = []
    
    for line in code.splitlines():
        splitcode.append(line)
    
    try:
        compile(splitcode[len(splitcode)-1],"<stdin>","eval")
        splitcode[len(splitcode)-1] = f"return {splitcode[len(splitcode)-1]}"
    except:
        pass
    
    parsedcode = []

    for line in splitcode:
        parsedcode.append("  "+line)

    parsedcode = "\n".join(parsedcode)

    fn = f"async def eval_fn():\n{parsedcode}"

    exec(fn,env)

    try:
        output = (await eval("eval_fn()",env))
        ecolor = discord.Color.green()
        outname = "Output"
    except Exception as error:
        output = error.__class__.__name__+": "+str(error)
        ecolor = discord.Color.red()
        outname = "Error"

    embed = discord.Embed(title="Eval",colour=ecolor)
    embed.add_field(name="Input",value="```py\n"+code+"\n```",inline=False)
    embed.add_field(name=outname,value="```\n"+str(output)+"\n```",inline=False)
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def load(ctx,extension):
    ctx.bot.load_extension("extensions."+extension)

@bot.command()
@commands.is_owner()
async def unload(ctx,extension):
    ctx.bot.unload_extension("extensions."+extension)

@bot.command()
@commands.is_owner()
async def reload(ctx,extension):
    ctx.bot.reload_extension("extensions."+extension)

def setup(client):
    client.add_command(_eval)
    client.add_command(load)
    client.add_command(unload)
    client.add_command(reload)