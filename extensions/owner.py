from discord.ext import commands as bot

@bot.command()
@bot.is_owner()
async def load(ctx,*,exts):
    extlist = exts.split()
    for ext in extlist:
        ctx.bot.load_extension("extensions."+ext)
    await ctx.send("Loaded "+", ".join(extlist))

@bot.command()
@bot.is_owner()
async def reload(ctx,*,exts):
    extlist = exts.split()
    for ext in extlist:
        ctx.bot.reload_extension("extensions."+ext)
    await ctx.send("Reloaded "+", ".join(extlist))

@bot.command()
@bot.is_owner()
async def math(ctx,*,mastermind_operation):
    result = eval(mastermind_operation)
    if result == "" or result == None:
        result = "`No Output`"
    else:
        result = "`"+str(result)+"`"
    await ctx.send(result)

def setup(botto):
    botto.add_command(load)
    botto.add_command(reload)
    botto.add_command(math)