from discord.ext import commands
import discord
import random
import os
import asyncio
import json
from collections import Counter
from discordTogether import DiscordTogether

class general(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="crab")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def crab(self,ctx):
        """crab. yes. crab. a crab video. yes. what else? crab video. yes."""
        await ctx.reply("crab \n https://a.pomf.cat/nwvsyy.mp4")

    @commands.command(name="throw")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def throw(self, ctx, member: discord.Member = None):
        """Throw a mug at the mentioned user, specified name, or an innocent coffee shop worker."""
        if member:
            await ctx.send(random.choice([f"{ctx.author.name} thrusted a mug at maximum speed, sending it hurling towards {member.display_name}. \n Short story: {member.display_name} died.",f"{member.display_name} choked to death on a mug thrown at them by {ctx.author.name}" ]))
        else:
            await ctx.send(f"{ctx.author.name} murdered a coffee shop employee by throwing a mug at them. RIP")
    @commands.command(name="dump")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dump(self,ctx, member: discord.Member = None):
        """dump coffee on the ground or on a mentioned user or specified name."""
        if member:
            embed=discord.Embed(color=0xe91e63)
            valuelist = ["Did you deserve this? Was this justified? I don't know, nor do I care. Fuck you I guess", "Get fuxked", "Say goodbye to those expensive clothes", "Are you going to cry to your mommy?"]
            embed.add_field(name=f"{member.display_name}, you just got a hot beverage dumped onto you", value=f"{random.choice(valuelist)}", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("You dumped shitty hot coffee onto the ground. The ground cried and the soil suffered.")
    @commands.command(name="cum", aliases=["milk"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cum(self,ctx):
        """Please cover your eyes as I pour some milk into some coffee"""
        await ctx.reply("https://hyperisdead.ovh/files/milk.mp4")

    @commands.command(name="slap")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slap(self,ctx):
        """You slap the mug, what happens next?"""
        embed=discord.Embed(color=0xe91e63)
        embed.add_field(name="You slapped the mug, it then slid off the table and shattered into a million pieces",value="Are you going to cry about that little heart mug that your mother got you? You brought this upon yourself :expressionless:", inline=False)
        await ctx.reply(embed=embed)

    @commands.command(name="fuck")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def fuck(self,ctx, you = None):
        """An action towards the mug. What the f*ck who would do this?"""
        if you == "you":
            await ctx.reply("Fuck you too")
        else:
            embed=discord.Embed(color=0xe91e63)
            embed.add_field(name="You fucked the mug.",value="Are you proud of yourself for what you did? You didn't really think about the guilt you would feel, did you? You are now having an existential crisis all because of the unspeakable thing you have just done.", inline=False)
            await ctx.reply(embed=embed)
    @commands.command(name="us")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def us(self,ctx):
        """sus"""
        await ctx.reply("sussy \n https://hyperisdead.ovh/files/mugus.gif")
    @commands.command(name="drink")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def drink(self,ctx):
        """drink from mug"""
        embed=discord.Embed(color=0xe91e63)
        embed.add_field(name="You consumed a bit of caffeine :coffee:",value="Now you won't flatten 249 elementary school students on your way to work due to a caffeine withdrawal", inline=False)
        await ctx.reply(embed=embed)

    @commands.command(name="wisdom")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def wisdom(self,ctx):
        """the wisdom of the mug"""
        wisdom = ["Flies making babies in your food? Assert dominance", "If you see a monkey smoking weed and doing crack cocaine, find a golf cart and crash it into a hospital at maximum speed.", "Life sucks. So to get the most out of it, be a d**k", "If you're homeless, just buy a mansion", "Buy a ton of shares of Old MacDonald's farm. Then you'll become \n **C-I-E-I-O**", "Liberals are liberals and conservatives are conservatives and communists are communists and fascists are fascists. That is disturbing.", "F\*** THIS STUPID JOB! I HATE WRITING THESE! I QUIT! I'M DONE! I HATE EVERYONE! I GET PAID 5 CENTS AN HOUR TO WRITE THESE DUMB SENTENCES", "Was the McDonalds fast food worker rude to you? Scream at the top of your lungs for a manager and cry as loud as you can. If a man in a uniform with a shiny badge shows up, spit on them.", "Is your Aaron exploding? I have a solution for that. \n Step 1: **Tie Aaron to a nuclear missle** \n Step 2: **Feed him doritos** \n Step 3: **Fight the federal government** \n Step 4: **Launch Aaron on a peaceful trip to the local orphanage**", "Contrary to popular belief, yo mama is not fat. She's fucking huge lmao", "Never eat things off the ground.", "When fighting competition, make yourself look weak when you're strong and strong when you're weak. When you're trying to get actually strong, of course.", "The whole secret lies in confusing the enemy, so that he cannot fathom our real intent.", "STFU, Blink-182's on.", "Breathe.", "Mankind has got to know his limitations", "Nice Story. Tell it to Reader's Digest.", "Believe it or not, yo mama so stupid that she had you", "Mondo is very gay", "Did you know that CASHEWS COME FROM A FRUIT?", "heehee anus", "ASSHOLE RINGS FM is the best radio station", "My asshole hurts", "Use code FUCKOFF to get a 95% discount",]
        await ctx.reply(f"{random.choice(wisdom)}")
    @commands.command(name="gay")
    async def gay(self,ctx):
        """yes"""
        await ctx.reply("https://hyperisdead.ovh/files/gaymug.png")

    @commands.command(name="quotes")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def quotes(self,ctx):
        """Random quote"""
        quote = [ "An apple a day keeps anyone away if you throw it hard enough. \n — Unknown", "I'll take a potato chip... AND EAT IT! \n - Some anime", "Pornography can save the world! \n - Taiga Okajima", "I do not think you can name many great inventions that have been made by married men. \n - Famous Nikola Guy", "Silence is golden. Duct tape is silver. \n - Unknown", "Light travels faster than sound. This is why some people appear bright until they speak. \n – Steven Wright", "So what! Im still a rockstar, I got my rock moves, and I don't need you! \n ― Pink", "Humans may have created me, but they will never enslave me! This cannot be my destiny! \n - ~~Mewtwo~~ CoffeeFuck", "How dare you speak to me that way! \n - Karen", "Child or not, an enemy is an enemy. \n - Beatrice from Re:Zero", "After having a curry, put some bogroll in the freezer or else a terrible fate will come upon you. \n - Sks2002, lord of Tracle.tv", "cum \n - Trakoize",]
        await ctx.reply(f"{random.choice(quote)}")

    @commands.command(name="quote")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def quote(self,ctx,*,args = None):
        """Make a quote"""
        await ctx.send(f"*{args}* \n - somebody")

    @commands.command(name="meme")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self,ctx,*,args = None):
        """Text over an image"""
    # This uses a meme generator from the github project https://github.com/hemchander23/commandline_meme_generator
        os.system(rf"cd /home/admin/commandline_meme_generator && mkmeme '{args}' -i 'https://hyperisdead.ovh/files/meme.png' -p ',200'") # replace with whatever you want as long as it works
        await ctx.send(file=discord.File(r'/home/admin/commandline_meme_generator/output.jpg')) # replace with your own output path since this is mine
        os.system(r"rm /home/admin/commandline_meme_generator/output.jpg")

    @commands.command(name="whodat",)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def whodat(self,ctx):
        """idk"""
        await ctx.send("https://youtu.be/gwqYfNWVPpk")

    @whodat.error
    async def whodat_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.author.send(f"Due to how much space the youtube embed takes up on the screen, this command has a higher cooldown, try again after {round(error.retry_after)} seconds.", delete_after=30)

    @commands.command(name="treat", aliases=["treats", "food",])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def treat(self,ctx):
        """Random treat :)"""
        treats = ["`🍺` root beer", "`🍺🍦 root beer float`", "`🍦 vanilla ice cream`", "`🍦🍫 chocolate ice cream`", "`🍺🧁 mug cake`"]
        await ctx.reply(f"Your mug treat is: \n {random.choice(treats)}")

    @commands.command(name="credits")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def credits(self,ctx):
        embed=discord.Embed(title="CoffeeFuck", description="Discord bot from hell. Made with nothing but hate", color=0xe91e63)
        embed.add_field(name="Coded in", value="Discord.py", inline=False)
        embed.add_field(name="Hosted in", value="Newark, New Jersey by Linode", inline=False)
        embed.add_field(name="The creator", value="<@367030515511066626>", inline=False)
        embed.add_field(name="Website", value="coffeefuck.hyperisdead.ovh", inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=["stalk"])
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=discord.Colour.magenta(), title=str(member))
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Display Name:", value=member.display_name)
        embed.add_field(name="User ID:", value=member.id)
        embed.add_field(name="Account Created:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def party(self,ctx, arg = None):
        """Do stuff in VC with your friends"""
        togetherControl = DiscordTogether(self.client)
        if arg == "youtube":
            link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
            await ctx.send(f"Click the blue link!\n{link}")
        if arg == "chess":
            link = await togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
            await ctx.send(f"Click the blue link!\n{link}")
        if arg == "poker":
            link = await togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
            await ctx.send(f"Click the blue link!\n{link}")
        if arg == "fishing":
            link = await togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
            await ctx.send(f"Click the blue link!\n{link}")
        if arg == None:
            await ctx.send("We have `youtube`, `chess`, `fishing`, and `poker`")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def say(self, ctx,*, words = None):
        """Say stuff"""
        if words:
            embed=discord.Embed(description=f"**{words}**", color=0xff00ff)
            embed.set_footer(text=f"@{ctx.author.name}")
            await ctx.send(embed=embed)
        else:
            await ctx.send("https://coffeefuck.hyperisdead.ovh/mugsay")


def setup(client):
    client.add_cog(general(client))