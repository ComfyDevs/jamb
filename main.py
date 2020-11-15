from discord.ext import commands

class JAMB(commands.Bot):
    token = "lmao learn d.py"

bot = JAMB(command_prefix=["JAMB ","jamb ","Jamb "])

bot.remove_command("help")

def loadExts(extlist):
    for ext in extlist:
        bot.load_extension("extensions."+ext)

loadExts(["misc","help","owner"])

bot.run(open("tok","r").read())