from discord.ext import commands
import discord
import time
class misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS main(
            touch_count TEXT,
            server_count TEXT
            )
            ''')
    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("Poof!")
        embed=discord.Embed()
        ping = (time.monotonic() - before) * 1000
        embed.add_field(name="I farted", value="The dangerous fart traveled for {} message milliseconds".format(int(ping - 20)))
        await ctx.reply(embed=embed)
        await ctx.send(f"And the client latency is {round(self.client.latency * 1000)}ms")
    @commands.command(aliases=["feedback", "suggestions"])
    async def suggest(self,ctx,*,arg = None):
        if arg == None:
            embed=discord.Embed(title="Suggest stuff", url="https://forms.gle/4ruRYMErcsFaeZhD6", description="If you are adding something to \"wisdom\" or \"quotes\", please specify so.")
            embed.add_field(name="Example:", value="Wisdom text: If a tree is running, you're probably on durgs", inline=False)
            embed.set_footer(text="Thank you for making the bot less of a boring piece of crap :smile:")
            await ctx.send(embed=embed)
        else:
            await ctx.send("This command doesn't accept submissions. Please run this command again without specifying anything and click on the \"Suggest stuff\" title.")
    @commands.command(aliases=["stalk"])
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
    async def discord(self,ctx):
        await ctx.reply("check ur dms")
        await ctx.author.send("https://discord.gg/GBuqdunrEr")

    @commands.is_owner()
    @commands.command()
    async def ownersay(self, ctx,*,arg):
        fire = self.client
        channel = fire.get_channel(726861129976119370)
        await channel.send(f"{arg}")
def setup(client):
    client.add_cog(misc(client))
