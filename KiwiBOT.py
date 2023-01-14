#!/usr/bin/env python3

import discord, random
from discord.ext import commands
from datetime import timedelta

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

#Limit Links
f = open("no_links.txt", "r")
lst = f.read().split("\n")
f.close()
nolinks = lst[:-1]
#Word Filter
f = open("banned_words.txt", "r")
bannedwrds = f.read().split("\n") 
f.close()
bannedwords = bannedwrds[:-1]
#Ip Grabber Section
f = open("ip_grabbers.txt", "r")
lst = f.read().split("\n")
f.close()
grabbies = lst[:-1]
#Link shortner Section
f = open("link_shortners.txt", "r")
lst = f.read().split("\n")
f.close()
shorties = lst[:-1]

@bot.event
async def on_ready():
    print("KiwiBOT is ready.")

### Chat Filter Beginning
@bot.event
async def on_message(msg):
    for text in nolinks:
        if "Waddler" not in str(msg.author.roles) and text in str(msg.content.lower()):
            await msg.reply("You don't have permission to send that, as you are not a waddler! ._.")
            await msg.delete()
            return
    for shit in bannedwords:
        if "KiwiBOT" not in str(msg.author.roles) and shit in str(msg.content.lower()):
            await msg.reply("Hold up....")
            channel = bot.get_channel(448686989286572032)
            await channel.send(f"**User**: {msg.author.mention}\n**Questionable message sent**: {msg.content}\n**Room**: {msg.channel.mention}\t**Penalty**: 1 minute timeout!")
            await msg.delete()
            await msg.author.timeout(timedelta(minutes = 1), reason = "Naughty words")
            return
    for instance in grabbies:
        if "KiwiBOT" not in str(msg.author.roles) and instance in str(msg.content.lower()):
            await msg.reply("Hold up.... You just sent an IP Grabber, you dirty bastard!")
            channel = bot.get_channel(448686989286572032)
            await channel.send(f"**User**: {msg.author.mention}\n**IP grabber sent**: {msg.content}\n**Room**: {msg.channel.mention}\t**Penalty**: 30 minute timeout!")
            await msg.delete()
            await msg.author.timeout(timedelta(minutes = 30), reason = "IP grabber sent")
            return
    for shortner in shorties:
        if "KiwiBOT" not in str(msg.author.roles) and shortner in str(msg.content.lower()):
            await msg.reply("Hold up.... No Link Shortners Permitted!")
            channel = bot.get_channel(448686989286572032)
            await channel.send(f"**User**: {msg.author.mention}\n**Link Shortner Sent**: {msg.content}\n**Room**: {msg.channel.mention}")
            await msg.delete()
            return

    await bot.process_commands(msg) #Without this line, commands are broken.
### Chat Filter End

@bot.command()
async def ping(ctx):
    await ctx.reply(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def sum(ctx, arg1, arg2):
    await ctx.send(f"Sum: {int(arg1) + int(arg2)}")


def dice_roll():
    dice_possibilites = [1, 2, 3, 4, 5, 6]
    dice_roll = str(random.choices(dice_possibilites))
    printabledice = dice_roll.replace("]","").replace("[","")
    return printabledice


def coin_toss():
    flip_possibilites = ["Heads", "Tails"]
    flip = str(random.choices(flip_possibilites))
    printableflip = flip.replace("]","").replace("[","").replace("'","")
    return printableflip

@bot.command()
async def flipcoin(ctx):
    await ctx.reply(f"**{coin_toss()}**")

@bot.command()
async def roll(ctx):
    await ctx.reply(f"**{dice_roll()}**")

@bot.command()
async def manual(ctx):
    await ctx.reply(f"$roll to roll a dice\n$flipcoin to flip a coin\n$ping to check bot latency")

t = open("token", "r")
tr = t.read()
t.close()
bot.run(tr)
