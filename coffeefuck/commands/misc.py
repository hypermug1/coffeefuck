from discord.ext import commands
import discord
import time
import asyncio
class misc(commands.Cog):
    """ Unimportant Garbage """
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        message = await ctx.send("Fuck")
        await message.edit(content="Pong")

    @commands.command(aliases=["feedback", "suggestions"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def suggest(self,ctx,*,arg = None):
        if arg == None:
            embed=discord.Embed(title="Suggest stuff", url="https://forms.gle/4ruRYMErcsFaeZhD6", description="If you are adding something to \"wisdom\" or \"quotes\", please specify so.")
            embed.add_field(name="Example:", value="Wisdom text: If a tree is running, you're probably on durgs", inline=False)
            embed.set_footer(text="Thank you for making the bot less of a boring piece of crap :smile:")
            await ctx.send(embed=embed)
        else:
            await ctx.send("This command doesn't accept submissions. Please run this command again without specifying anything and click on the \"Suggest stuff\" title.")
    @commands.command(aliases=["stalk"])
    @commands.cooldown(1,5,commands.BucketType.user)
    async def userinfo(self,ctx, *, user: discord.User = None):
        if user is None:
            user = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=0xdfa3ff, description=user.mention)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
        embed.set_footer(text='ID: ' + str(user.id))
        await ctx.send(embed=embed)
    @commands.command(aliases=["discordserver", "support"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def discord(self,ctx):
        await ctx.reply("check ur dms")
        await ctx.author.send("https://discord.gg/GBuqdunrEr")
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invite(self, ctx):
        await ctx.send("sent in dms", delete_after=5)
        await ctx.author.send("https://discord.com/oauth2/authorize?client_id=859188359712866315&permissions=134596672&scope=bot")
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def info(self, ctx):
        await ctx.send("Greetings. Curious it seems?", delete_after=3)
        await asyncio.sleep(3)
        embed=discord.Embed(title="How it started", description="Boredom", color=0xdc8add)
        embed.set_author(name="CoffeeFuck", url="https://hyperisdead.ovh#coffeefuck", icon_url="https://cdn.discordapp.com/avatars/859188359712866315/be40e86cf9c3102d557ee33bfa46da02.webp?size=80")
        embed.add_field(name="Hardware", value="BuyVM server located in New York, has unmetered bandwidth", inline=False)
        embed.add_field(name="Code", value="Made in Python with the Pycord Discord API wrapper", inline=False)
        embed.add_field(name="Crying children in:", value=f"Like {str(len(self.client.guilds))} servers", inline=False)
        embed.add_field(name="Complaints ", value="Feed them to the paper shredder. Go cry about it.", inline=False)
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(misc(client))
