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
        await ctx.send("Red ๐ด ๐ sus ๐ฆ ๐ฆ. Red ๐ด ๐ด suuuus. I ๐๐ ๐ said ๐ค ๐ฃ ๐ฌ๐ฑ๐ฟ๐ฆ red ๐น ๐ด, sus ๐ฆ ๐ฆ, hahahahaha ๐คฃ ๐คฃ. Why ๐ค ๐ค arent you ๐๐ฏ ๐ laughing ๐ ๐? I ๐๐ ๐ฅ just made ๐ ๐ a reference ๐๐๐ ๐๐๐ to the popular ๐๐๐ ๐ video ๐น ๐น game ๐ฎ ๐ฎ โAmong ๐ท๐ด๐ ๐ฐ Us ๐จ ๐จโ! How can you ๐ ๐ not laugh ๐ ๐ at it? Emergeny meeting ๐ฏ ๐ค! Guys ๐ฆ ๐จ, this here guy ๐จ ๐ฑ๐ป๐จ๐ป doesnt laugh ๐คฃ โ๐๐ at my funny ๐๐ ๐บ๐๐ Among ๐ฐ ๐ฐ Us ๐จ ๐จ memes ๐ธ ๐! Lets ๐ ๐ beat โ๐๐ป ๐ฐ๐ him ๐ด ๐จ to death ๐๐ฅโ ๐! Dead ๐๐ โ  body ๐ ๐ reported โ ๐ง! Skip ๐ง ๐๐ผ! Skip ๐ง ๐ง! Vote ๐ ๐ blue ๐ ๐! Blue ๐ ๐ was not an impostor ๐ ๐ . Among ๐ ๐๐ฝ๐ฐ us ๐จ ๐จ in a nutshell ๐  ๐  hahahaha ๐๐๐ ๐. What?! Youre still ๐ค๐ ๐ค๐ not laughing ๐ ๐ your ๐ ๐ ass ๐ ๐ฐ off ๐ด ๐ดโ ? I ๐ ๐ made ๐ ๐ SEVERAL ๐ฏ ๐ฏ funny ๐๐๐ ๐โ references ๐๐๐ ๐ to Among ๐ฐ ๐๐จโโค๏ธโ๐จ๐ฉโโค๏ธโ๐ฉ Us ๐จ ๐บ๐ธ and YOU ๐๐ผ ๐๐๐ฅ STILL ๐ค๐ ๐ ARENT LAUGHING ๐ ๐๐๐ฆ??!!! Bruh โ  ๐ณ๐คฃ๐. Ya ๐๐ผ ๐ hear ๐")
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
