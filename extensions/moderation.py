import discord
from discord.ext import commands
import typing
bot = commands

@bot.command()
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, users: commands.Greedy[discord.Member], *, reason: typing.Optional[str] = "Breaking the rules!"):
    banned = []
    
    for user in users:
        banned.append(user.mention)
        await user.ban(reason=reason)
    if len(banned) == 1:
        verb = "has"
        bannedlist = banned[0]
    elif len(banned) > 1:
        lastbanned = banned[len(banned)-1]
        banned.pop(len(banned)-1)
        bannedlist = f"{', '.join(banned)} and {lastbanned}"
        verb = "have"
    
    if len(users) >= 1:
        await ctx.send(f"{bannedlist} {verb} been banned for reason: '{reason}'")
    else:
        await ctx.send("You must specify at least 1 person to ban!")

@bot.command()
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
async def kick(ctx, users: commands.Greedy[discord.Member], *, reason: typing.Optional[str] = "Breaking the rules!"):
    kicked = []
    
    for user in users:
        kicked.append(user.mention)
        await user.kick(reason=reason)
    if len(kicked) == 1:
        verb = "has"
        kickedlist = kicked[0]
    elif len(kicked) > 1:
        lastkicked = kicked[len(kicked)-1]
        kicked.pop(len(kicked)-1)
        kickedlist = f"{', '.join(kicked)} and {lastkicked}"
        verb = "have"
    
    if len(users) >= 1:
        await ctx.send(f"{kickedlist} {verb} been kicked for reason: '{reason}'")
    else:
        await ctx.send("You must specify at least 1 person to kick!")

def setup(client):
    client.add_command(ban)
    client.add_command(kick)