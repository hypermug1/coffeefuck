from discord.ext import commands
import discord
from discord import user
from discord import Member
import datetime
import time

class bot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["test"], brief="pings the bot",help="pings the bot")
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def ping(self,ctx):
        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        ping = round((time_2 - time_1) * 1000)
        embed=discord.Embed(title="Congrats you pinged the bot", description="WOW YOU DID SOMETHING")
        embed.add_field(name="THE BOT IS WORKING?? OH COOL", value=f"{ping}ms".format(ping), inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="discord",aliases=["discord,support,"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def discord(self,ctx):
        """Join the Discord"""
        embed=discord.Embed(title="Discord", colour=discord.Colour(0x9adbed), url="https://discord.gg/DdveATMbfp", description="Want to complain about things added intentionally or unintentionally? Join! Want to see what the heck is going on? Join! Want to give feedback that might be ignored? Join!")
        await ctx.author.send(embed=embed)
        await ctx.send("Sent in DMs. Join the server or else I will use bitcoin to send poop to your doorstep.", delete_after=8)

    @commands.command(name="invite")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def invite(self,ctx):
        """Bot invite"""
        embed=discord.Embed(title="Bot invite", colour=discord.Colour(0x9adbed), url="https://discord.com/oauth2/authorize?client_id=859188359712866315&permissions=134596672&scope=bot", description="Like the bot? Here's your invite")
        await ctx.author.send(embed=embed)
        await ctx.send("Sent in DMs. Invite or else I will use bitcoin to send poop to your doorstep.", delete_after=8)

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    async def purge(self,ctx, amount=0):
        """Specify how many messages the bot should delete and they will be deleted. Requires \"manage messages\" permissions """
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send("purged",delete_after=2)

    @commands.command(name="suggestion",aliases=["suggestions","feedback"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def suggestion(self,ctx,*,arg=None):
        """Suggest a command or addition to an existing one. There is no guarantee it will be added"""
        if arg == None:
            await ctx.author.send("https://forms.gle/4ruRYMErcsFaeZhD6")
        elif arg != None:
            await ctx.reply("Suggestions aren't accepted through the bot. Run this command again without specifying anything")
def setup(client):
    client.add_cog(bot(client))
