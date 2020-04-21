import discord
from discord.ext import commands
import json
import os
import collections.abc
import time

client = commands.Bot(command_prefix = '!')
os.chdir('/Users/jesse.brower/projects/robo-isabelle')

@client.event
async def on_ready():
    print('Robo-Isabelle is ready.')

@client.command()
async def myfc(ctx, arg):

    with open('users.json', 'r') as d:
        users = json.load(d)

    await add_user(users, ctx.author)
    await update_code(users, ctx.author, arg)

    with open('users.json', 'w') as d:
        json.dump(users, d)

    await ctx.send(f'{ctx.author} just added {arg} to the database.')
    print(f'{ctx.author} just added {arg} to the database.')

@client.command()
async def get_codes(ctx):

    with open('users.json', 'r') as d:
        users = json.load(d)

    embed = discord.Embed(title="Friend Codes")

    for user in users:

        embed.add_field(name=users[f'{user}']['username'], value=users[f'{user}']['code'], inline=False)

    await ctx.send(embed=embed)

async def add_user(users, user):

    if not f'{user.id}' in users:

        users[f'{user.id}'] = {}
        users[f'{user.id}']['username'] = str(user)
        users[f'{user.id}']['turnips'] = "n/a"
        users[f'{user.id}']['time'] = "n/a"

async def update_code(users, user, code):

    users[f'{user.id}']['code'] = str(code)

@client.command()
async def myPrice(ctx, arg):

    with open('users.json', 'r') as d:
        users = json.load(d)

    await add_user(users, ctx.author)
    await update_turnips(users, ctx.author, arg)

    with open('users.json', 'w') as d:
        json.dump(users, d)

    await ctx.send(f'{ctx.author} updated their turnips price to {arg}.')
    print(f'{ctx.author} updated their turnips price to {arg}.')

async def update_turnips(users, user, turnips):

    users[f'{user.id}']['turnips'] = str(turnips)
    users[f'{user.id}']['time'] = time.asctime(time.localtime(time.time()))

@client.command()
async def priceCheck(ctx):

    with open('users.json', 'r') as d:
        users = json.load(d)

    embed = discord.Embed(title="Turnips Prices")

    for user in users:
        if users[f'{user}']['turnips'] != 'n/a':

            embed.add_field(name=users[f'{user}']['username'], value=users[f'{user}']['turnips'], inline=False)
            embed.add_field(name='Time Stamp:', value=users[f'{user}']['time'], inline=False)

    await ctx.send(embed=embed)

client.run(Your_Token)