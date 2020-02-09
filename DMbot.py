import discord
from discord.ext.commands import bot
from discord import game
from discord.ext import commands
import asyncio
import platform
import colorsys
import random
import time

client = commands.Bot(command_prefix = '+', case_insensitive=True)
Client = discord.client
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Created by Soodalpie')
    


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="이름", value=user.name, inline=True)
    embed.add_field(name="아이디", value=user.id, inline=True)
    embed.add_field(name="상태", value=user.status, inline=True)
    embed.add_field(name="높은역할", value=user.top_role)
    embed.add_field(name="들어옴", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    
@commands.has_permissions(administrator=True)
@client.command(pass_context = True)
async def send(ctx, *, content: str):
        for member in ctx.message.server.members:
            try:
                await client.send_message(member, content)
                await client.say("DM 전송 완료 : {} :white_check_mark:  ".format(member))
            except:
                print("can't")
                await client.say("DM 전송 불가 : {} :x: ".format(member))


client.run("Njc1NzE2MTE0MTI2MjA5MDM1.Xj7Lxw.aDCJ2m6tp68YdfEnV2No-hO6V0k")
