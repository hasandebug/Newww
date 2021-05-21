import discord, time, json, discord.ext, webbrowser, colorama, pynput, random, asyncio
from discord import *
from time import *
from json import *
from discord.ext import commands
from colorama import Fore, Style
from asyncio import *

def InviteServer():
    webbrowser.open('https://discord.gg/nc6Y6UR9rU', new=2)

with open ('config.json') as f:
    data = json.load(f)

InviteServer()

client_prefix = '$' # Ya can change this

token = data['token']

client = commands.Bot(
description='Discord Self Bot', 
command_prefix= f'{client_prefix}',
self_bot=True
)
client.remove_command('help')

@client.event
async def on_connect():
    print()
    print(f'{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.CYAN}Dank Memer Farmer made by "Destinity')
    print(f'{Fore.WHITE}[ {Fore.YELLOW}- {Fore.WHITE}] {Fore.CYAN}Join my discord server for help https://discord.gg/nc6Y6UR9rU')
    print(f'{Fore.WHITE}[ {Fore.YELLOW}! {Fore.WHITE}] {Fore.CYAN}Logged in as {client.user.name}#{client.user.discriminator}')
    print(f'{Fore.WHITE}[ {Fore.YELLOW}+ {Fore.WHITE}] {Fore.CYAN}Type {client_prefix}begin to start...' + Style.RESET_ALL)
    print()
    print(f'{Fore.WHITE}]{Fore.WHITE}========================={Fore.WHITE}[')
    print()

@client.command()
async def help(ctx):
    await ctx.send(f':heart: **Type {client_prefix}begin to start farming!** Join my discord server if you need more help')
    await ctx.send(f':heart: **https://discord.gg/nc6Y6UR9rU** < Made by "Destinity')  # Change this = gay
    print(f'{Fore.WHITE}- {Fore.RED}Executed command "help"')

@client.command()
async def fuck(ctx):
    await ctx.send(f':rainbow_flag: Fucked')
    print(f'{Fore.WHITE}- {Fore.RED}Executed command "fuck"')

@client.command()
async def credits(ctx):
    await ctx.send(f'Discord Bot Farmer made by **"Destinity** -> **https://www.youtube.com/channel/UCRjcgy4s6rTcbyCK58ga9sA** Prefix: **{client_prefix}**')
    print(f'{Fore.WHITE}- {Fore.RED}Executed command "credits"')

@client.event
async def on_message(message):
    channel_id = 844858245410586664 # Change this
    channel = client.get_channel(channel_id)
    
    
    if message.author.id == 270904126974590976 and message.channel.id == channel_id:
        if "christmas tree" in message.content:
            await asyncio.sleep(1)
            await channel.send("christmas tree")
        elif "north pole" in message.content:
            await asyncio.sleep(1)
            await channel.send("north pole")
        elif "christmas card" in message.content:
            await asyncio.sleep(1)
            await channel.send("christmas card")
        elif "big bait catches big fish" in message.content:
            await asyncio.sleep(1)
            await channel.send("big bait catches big fish")
        elif "What type of meme do you want to post?" in message.content:
            await asyncio.sleep(1)
            await channel.send("k")
        elif "yes please" in message.content:
            await asyncio.sleep(1)
            await channel.send("yes please")
        elif "oh look a dragon" in message.content:
            await asyncio.sleep(1)
            await channel.send("oh look a dragon")
        elif "oh frick a dragon" in message.content:
            await asyncio.sleep(1)
            await channel.send("oh frick a dragon")
        elif "pls no eating me" in message.content:
            await asyncio.sleep(1)
            await channel.send("pls no eating me")
        elif "woah those are some toothers" in message.content:
            await asyncio.sleep(1)
            await channel.send("woah those are some toothers") 
        elif "why didn't I just go fishing" in message.content:
            await asyncio.sleep(1)
            await channel.send("why didn't I just go fishing")
        elif "eat lead dragon" in message.content:
            await asyncio.sleep(1)
            await channel.send("eat lead dragon")    
        elif "imma kill this dragon" in message.content:
            await asyncio.sleep(1)
            await channel.send("imma kill this dragon")
        elif "pls no eating me" in message.content:
            await asyncio.sleep(1)
            await channel.send("pls no eating me")                    
        elif "make snow angel" in message.content:
            await asyncio.sleep(1)
            await channel.send("make snow angel")                                             
        elif "frick off" in message.content:
            await asyncio.sleep(1)
            await channel.send("frick off")
        elif "glub glub glub" in message.content:
            await asyncio.sleep(1)
            await channel.send("glub glub glub")
        elif "mistletoe" in message.content:
            await asyncio.sleep(1)
            await channel.send("mistletoe")
        elif "krampus is a nerd" in message.content:
            await asyncio.sleep(1)
            await channel.send("krampus is a nerd")
        elif "push" in message.content:
            await asyncio.sleep(1)
            await channel.send("push")
        elif "dibs" in message.content:
            await asyncio.sleep(1)
            await channel.send("dibs")
        elif "happy holidays" in message.content:
            await asyncio.sleep(1)
            await channel.send("happy holidays")
        elif "throw snowball" in message.content:
            await asyncio.sleep(1)
            await channel.send("throw snowball")
        elif "get the camera ready" in message.content:
            await asyncio.sleep(1)
            await channel.send("get the camera ready")
        elif "whoville sucks" in message.content:
            await asyncio.sleep(1)
            await channel.send("whoville sucks")
        elif "build snowman" in message.content:
            await asyncio.sleep(1)
            await channel.send("build snowman")
        elif "hook line sinker" in message.content:
            await asyncio.sleep(1)
            await channel.send("hook line sinker")
        elif "attic" in message.content:
            await asyncio.sleep(1)
            await channel.send('attic')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "attic"')
        elif "sewer" in message.content:
            await asyncio.sleep(1)
            await channel.send("sewer")
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "sewer"')
        elif "tree" in message.content:
            await asyncio.sleep(1)
            await channel.send("tree")
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "tree"')
        elif "discord" in message.content:
            await asyncio.sleep(1)
            await channel.send('discord')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "discord"')
        elif "bushes" in message.content:
            await asyncio.sleep(1)
            await channel.send('bushes')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "bushes"')
        elif "air" in message.content:
            await asyncio.sleep(1)
            await channel.send('air')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "air"')
        elif "mailbox" in message.content:
            await asyncio.sleep(1)
            await channel.send('mailbox')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "mailbox"')
        elif "fridge" in message.content:
            await asyncio.sleep(1)
            await channel.send('fridge')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "fridge"')
        elif "laundromat" in message.content:
            await asyncio.sleep(1)
            await channel.send('laundromat')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "laundromat"')
        elif "grass" in message.content:
            await asyncio.sleep(1)
            await channel.send('grass')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "grass"')
        elif "dumpster" in message.content:
            await asyncio.sleep(1)
            await channel.send('dumpster')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "dumpster"')
        elif "shoe" in message.content:
            await asyncio.sleep(1)
            await channel.send('shoe')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "shoe"')
        elif "pantry" in message.content:
            await asyncio.sleep(1)
            await channel.send('pantry')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "pantry"')
        elif "hospital" in message.content:
            await asyncio.sleep(1)
            await channel.send('hospital')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "hospital"')
        elif "car" in message.content:
            await asyncio.sleep(1)
            await channel.send('Bruh, this sucks! give me something other...')
            print(f'{Fore.WHITE}- {Fore.RED}Too dangerous search, answering with something other')
        elif "area51" in message.content:
            await asyncio.sleep(1)
            await channel.send('Bruh, this sucks! give me something other...')
            print(f'{Fore.WHITE}- {Fore.RED}Too dangerous search, answering with something other')
        elif "purse" in message.content:
            await asyncio.sleep(1)
            await channel.send('Bruh, this sucks! give me something other...')
            print(f'{Fore.WHITE}- {Fore.RED}Too dangerous search, answering with something other')
        elif "bank" in message.content:
            await asyncio.sleep(1)
            await channel.send('Bruh, this sucks! give me something other...')
            print(f'{Fore.WHITE}- {Fore.RED}Too dangerous search, answering with something other')
        elif "dresser" in message.content:
            await asyncio.sleep(1)
            await channel.send('dresser')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "dresser"')
        elif "vacuum" in message.content:
            await asyncio.sleep(1)
            await channel.send('vacuum')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "vacuum"')
        elif "glovebox" in message.content:
            await asyncio.sleep(1)
            await channel.send('glovebox')
            print(f'{Fore.WHITE}- {Fore.RED}Answered For search as "glovebox"')

    await client.process_commands(message) # Fixing commands... Don't remove it
    

# Yeah, after 2 hours imma try to search for something but it's hard....
# I cant get it bye
# Update: After a day i got it lmao
# I was wrong
# After 3 days i got it yay FINALLY
# Im uploading this to mega.nz lol


@client.command()
async def begin(ctx):
    print()
    print(f'{Fore.WHITE}]{Fore.WHITE}========================={Fore.WHITE}[')
    print()
    print(f'{Fore.WHITE}[ {Fore.CYAN}x {Fore.WHITE}] {Fore.GREEN}Farming Commands...')
    print()
    print(f'{Fore.WHITE}]{Fore.WHITE}========================={Fore.WHITE}[')
    print()

    while True:
        await ctx.send("pls hunt")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "pls hunt"')
        await asyncio.sleep(6)
        await ctx.send("pls search")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "pls seach"')
        await asyncio.sleep(3)
        await ctx.send("pls fish")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "pls fish"')
        await asyncio.sleep(10)
        await ctx.send("pls beg")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "pls beg"')
        await asyncio.sleep(21)
        await ctx.send("pls search")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "pls search"')
        await asyncio.sleep(6)
        await ctx.send("pls pm")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "pls pm"')
        await asyncio.sleep(2)
        await ctx.send("k")
        print(f'{Fore.WHITE}- {Fore.RED}Answered Fore search as "k"')
        await ctx.send("pls beg")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "pls beg"')
        await asyncio.sleep(2)
        await ctx.send("pls dep all")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "pls dep all"')
        await asyncio.sleep(16)

client.run(token, bot=False)
