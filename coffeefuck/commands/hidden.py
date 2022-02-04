from discord.ext import commands
import discord
import asyncio
import subprocess
import random
import os
import typing
import praw
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from discord_together import DiscordTogether
class hidden(commands.Cog):
    """Hidden things within the bot. Go try running some words like `mug hidden wordhere`"""
    def __init__(self, client,):
        self.client = client
        
    
    @commands.group()
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def hidden(self,ctx,):
        pass
    @hidden.command()
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def chaogamer(self,ctx):
        await ctx.send("Hi i'm chaogamer, a catholic priest, I do not touch children")
    @hidden.command(name="borisjohnson",aliases=["boris", "johnson"])
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def boris_johnson(self,ctx):
        await ctx.send("Boris Johnson is a fucking cunt")
    @hidden.command()
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def wordhere(self,ctx):
        await ctx.send("You found a word!")
    @hidden.command()
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def nft(self,ctx):
        await ctx.send("Trash")
    @hidden.command()
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def drugs(self,ctx):
        await ctx.send("World go spinny")
    @hidden.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def sus(self,ctx):
        await ctx.send("Red 🔴 📛 sus 💦 💦. Red 🔴 🔴 suuuus. I 👁👄 👁 said 🤠🗣 💬👱🏿💦 red 👹 🔴, sus 💦 💦, hahahahaha 🤣 🤣. Why 🤔 🤔 arent you 👉😯 👈 laughing 😂 😂? I 👁🍊 👥 just made 👑 👑 a reference 👀👄🙀 👀👄🙀 to the popular 👍😁😂 😂 video 📹 📹 game 🎮 🎮 “Among 🇷🇴🎛 💰 Us 👨 👨”! How can you 👈 👈 not laugh 😂 😂 at it? Emergeny meeting 💯 🤝! Guys 👦 👨, this here guy 👨 👱🏻👨🏻 doesnt laugh 🤣 ☑😂😅 at my funny 😃😂 🍺😛😃 Among 💰 💰 Us 👨 👨 memes 🐸 😂! Lets 🙆 🙆 beat ✊👊🏻 😰👊 him 👴 👨 to death 💀💥❓ 💀! Dead 💀😂 ☠ body 💃 💃 reported ☎ 🧐! Skip 🐧 🏃🏼! Skip 🐧 🐧! Vote 🔝 🔝 blue 💙 💙! Blue 💙 💙 was not an impostor 😎 😠. Among 😂 🙆🏽🅰 us 👨 👨 in a nutshell 😠 😠 hahahaha 😂👌👋 😂. What?! Youre still 🤞🙌 🤞🙌 not laughing 😂 😂 your 👉 👉 ass 🍑 🅰 off 📴 📴☠? I 👁 👁 made 👑 👑 SEVERAL 💯 💯 funny 😀😂😛 😃❓ references 👀👄🙀 📖 to Among 💰 💑👨‍❤️‍👨👩‍❤️‍👩 Us 👨 🇺🇸 and YOU 👈🏼 😂👉🔥 STILL 🤞🙌 🙄 ARENT LAUGHING 😂 😂😎💦??!!! Bruh ⚠ 😳🤣😂. Ya 🙏🎼 🙀 hear 👂")
    @hidden.command()
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def penis(self,ctx):
        await ctx.send("Haha funny word")
    @hidden.command(name="sixnine",aliases=["69", "420"])
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def sixnine(self,ctx):
        await ctx.send("Funny number")
    @hidden.command(name="mom",aliases=["mum"])
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def mom(self,ctx):
        await ctx.send("Guess what? I'll do your mom")
    @hidden.command(name="dad",aliases=["daddy", "father"])
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def dad(self,ctx):
        await ctx.send("Fatherless")
    @hidden.command()
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def bullshit(self,ctx):
        await ctx.send("Bullshit!")
    @commands.cooldown(10, 10, commands.BucketType.user)
    async def hello(self,ctx):
        await ctx.send("Fuck off")
def setup(client):
    client.add_cog(hidden(client))
