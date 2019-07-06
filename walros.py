import discord
from discord.ext import commands
import random as r
import os
from dotenv import load_dotenv
from spell_data import spellbook

# ======================================================= >>
#
#  █     █░ ▄▄▄       ██▓     ██▀███   ▒█████    ██████ 
# ▓█░ █ ░█░▒████▄    ▓██▒    ▓██ ▒ ██▒▒██▒  ██▒▒██    ▒ 
# ▒█░ █ ░█ ▒██  ▀█▄  ▒██░    ▓██ ░▄█ ▒▒██░  ██▒░ ▓██▄   
# ░█░ █ ░█ ░██▄▄▄▄██ ▒██░    ▒██▀▀█▄  ▒██   ██░  ▒   ██▒
# ░░██▒██▓  ▓█   ▓██▒░██████▒░██▓ ▒██▒░ ████▓▒░▒██████▒▒
# ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░▓  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
#   ▒ ░ ░    ▒   ▒▒ ░░ ░ ▒  ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░
#   ░   ░    ░   ▒     ░ ░     ░░   ░ ░ ░ ░ ▒  ░  ░  ░  
#     ░          ░  ░    ░  ░   ░         ░ ░        ░  
# ======================================================= >>
# Written By: Aarick-F
# A Discord Helper Bot for various D&D-related tasks
# The name Walros is taken from a wise, old, and snarky Wizard
# from the Dungeons & Dragons campaign dreamed up by Jody B.

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def makeEmbed(spell):
    spell_name = spell.upper()
    embed = discord.Embed(title=spell_name, color=0xff00ff)
    level = spellbook[spell.lower()]["level"]
    components = spellbook[spell.lower()]["components"]
    casting_time = spellbook[spell.lower()]["casting time"]
    spell_range = spellbook[spell.lower()]["range"]
    target = spellbook[spell.lower()]["target"]
    effect = spellbook[spell.lower()]["effect"]
    duration = spellbook[spell.lower()]["duration"]
    saving_throw = spellbook[spell.lower()]["saving throw"]
    resistance = spellbook[spell.lower()]["spell resistance"]
    description = spellbook[spell.lower()]["description"]
    embed = discord.Embed(title=spell_name, color=0xff00ff)
    if len(level) > 0:
        embed.add_field(name="Level", value=level, inline=False)
    if len(components) > 0:
        embed.add_field(name="Components", value=components, inline=False)
    if len(casting_time) > 0:
        embed.add_field(name="Casting Time", value=casting_time, inline=False)
    if len(spell_range) > 0:
        embed.add_field(name="Range", value=spell_range, inline=False)
    if len(target) > 0:
        embed.add_field(name="Target", value=target, inline=False)  
    if len(effect) > 0:
        embed.add_field(name="Effect", value=effect, inline=False)
    if len(duration) > 0:
        embed.add_field(name="Duration", value=duration, inline=False)
    if len(saving_throw) > 0:
        embed.add_field(name="Saving Throw", value=saving_throw, inline=False)
    if len(resistance) > 0:
        embed.add_field(name="Spell Resistance", value=resistance, inline=False)
    if len(description) > 0:
        embed.add_field(name="Description", value=description, inline=False)
    return embed


bot = commands.Bot(command_prefix="$", description="An old man with a wealth of knowledge in magic")

@bot.event
async def on_ready():
    print("Logged in as: {}".format(bot.user.name))
    print("Bot ID: {}".format(bot.user.id))
    print("-" * 40)

bot.remove_command("help")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Walros", description="An old man with a disturbing amount of magical knowledge\nAuthor: Aarick-F\nList of commands are:", color=0xff00ff)
    embed.add_field(name="$spell 'spell name'", value="Returns details of requested spell", inline=False)
    embed.add_field(name="$roll20 <optional number of D20>", value="Rolls a D20 or multiple D20", inline=False)
    embed.add_field(name="$roll12 <optional number of D12>", value="Rolls a D12 or multiple D12", inline=False)
    embed.add_field(name="$roll8 <optional number of D8>", value="Rolls a D8 or multiple D8", inline=False)
    embed.add_field(name="$roll6 <optional number of D6>", value="Rolls a D6 or multiple D6", inline=False)
    embed.add_field(name="$roll4 <optional number of D4>", value="Rolls a D4 or multiple D4", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def spell(ctx, spell: str):
    # here we will define the logic that will
    # fetch the spell requested
    if spell.lower() in spellbook:
        embed = makeEmbed(spell.lower())
        await ctx.send(embed=embed)
    else:
        await ctx.send("That spell was not found.")

@bot.command()
async def roll20(ctx, *n):
    if n:
        amount = int(n[0])
        result = 0
        if amount < 10001:
            for i in range(amount):
                result += r.randint(1, 20)
            embed = discord.Embed(title="D20 Roll:", description=result, color=0xff00ff)
        else:
            embed = discord.Embed(title="Hell Naw", description="Sorry fam, go find my daughters first.", color=0xff00ff)
    else:
        embed = discord.Embed(title="D20 Roll:", description=r.randint(1, 21), color=0xff00ff)
    await ctx.send(embed=embed)

@bot.command()
async def roll12(ctx, *n):
    if n:
        amount = int(n[0])
        result = 0
        if amount < 10001:
            for i in range(amount):
                result += r.randint(1, 12)
            embed = discord.Embed(title="D12 Roll:", description=result, color=0xff00ff)
        else:
            embed = discord.Embed(title="Hell Naw", description="Sorry fam, go find my daughters first.", color=0xff00ff)
    else:
        embed = discord.Embed(title="D12 Roll:", description=r.randint(1, 13), color=0xff00ff)
    await ctx.send(embed=embed)

@bot.command()
async def roll10(ctx, *n):
    if n:
        amount = int(n[0])
        result = 0
        if amount < 10001:
            for i in range(amount):
                result += r.randint(1, 10)
            embed = discord.Embed(title="D10 Roll:", description=result, color=0xff00ff)
        else:
            embed = discord.Embed(title="Hell Naw", description="Sorry fam, go find my daughters first.", color=0xff00ff)
    else:
        embed = discord.Embed(title="D10 Roll:", description=r.randint(1, 11), color=0xff00ff)
    await ctx.send(embed=embed)

@bot.command()
async def roll8(ctx, *n):
    if n:
        amount = int(n[0])
        result = 0
        if amount < 10001:
            for i in range(amount):
                result += r.randint(1, 8)
            embed = discord.Embed(title="D8 Roll:", description=result, color=0xff00ff)
        else:
            embed = discord.Embed(title="Hell Naw", description="Sorry fam, go find my daughters first.", color=0xff00ff)
    else:
        embed = discord.Embed(title="D8 Roll:", description=r.randint(1, 9), color=0xff00ff)
    await ctx.send(embed=embed)

@bot.command()
async def roll6(ctx, *n):
    if n:
        amount = int(n[0])
        result = 0
        if amount < 10001:
            for i in range(amount):
                result += r.randint(1, 6)
            embed = discord.Embed(title="D6 Roll:", description=result, color=0xff00ff)
        else:
            embed = discord.Embed(title="Hell Naw", description="Sorry fam, go find my daughters first.", color=0xff00ff)
    else:
        embed = discord.Embed(title="D6 Roll:", description=r.randint(1, 7), color=0xff00ff)
    await ctx.send(embed=embed)

@bot.command()
async def roll4(ctx, *n):
    if n:
        amount = int(n[0])
        result = 0
        if amount < 10001:
            for i in range(amount):
                result += r.randint(1, 4)
            embed = discord.Embed(title="D4 Roll:", description=result, color=0xff00ff)
        else:
            embed = discord.Embed(title="Hell Naw", description="Sorry fam, go find my daughters first.", color=0xff00ff)
    else:
        embed = discord.Embed(title="D4 Roll:", description=r.randint(1, 5), color=0xff00ff)
    await ctx.send(embed=embed)

bot.run(TOKEN) 