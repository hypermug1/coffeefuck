from discord.ext import commands
import discord
import asyncio
import subprocess
import random
import os
import typing
import praw
from discord_together import DiscordTogether
class fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_message(self,message):
        mention = f'<@!{self.client.user.id}>'
        if mention == message.content:
            await message.author.send("fuck you <:psychofunny:859278377651404810>")
        elif "mug go fucking die in a ditch ngl" == message.content:
            await message.author.send("no u")
        elif "coffeefuck sucks" == message.content.lower():
            await message.author.send("no u suck")
        elif "i\'m gay" == message.content.lower() or "im gay" == message.content.lower():
            await message.author.send("congrats?")
        elif "sus" == message.content.lower():
            await message.author.send("sus is funny word xd")


    @commands.command(name="memer")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def memer(self,ctx,*,message = None):
    # This uses a meme generator from the github project https://github.com/hemchander23/
        await ctx.send("creating trash... gimme a second")
        async with ctx.typing():
            args = str(message)
            subprocess.run("cd /home/admin/commandline_meme_generator && mkmeme \"{}\" -i 'https://a.pomf.cat/iesrml.png' -p ',200' -o /home/admin/commandline_meme_generator/output.jpg".format(args),shell=True) # replace with whatever you want as long as it works
            await ctx.send(file=discord.File(r'/home/admin/commandline_meme_generator/output.jpg')) # replace with your own output path since this is mine
            subprocess.run(r"rm /home/admin/commandline_meme_generator/output.jpg", shell=True)

    @commands.command(name="slap")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slap(self,ctx, user: discord.User = None):
        if user is None:
            embed=discord.Embed(color=discord.Color.blue())
            embed.add_field(name="You slapped the mug, it then slid off the table and shattered into a million pieces",value="Are you going to cry about that little heart mug that your mother got you? You brought this upon yourself :expressionless:", inline=False)
            await ctx.reply(embed=embed)
        else:
            embed=discord.Embed(color=discord.Color.blue())
            embed.add_field(name="WHAM!",value=f"{user.name} got hit by a mug!", inline=False)
            await ctx.reply(embed=embed)
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def phucker(self, ctx):
        def check(message: discord.Message):
            return message.channel == ctx.channel and message.author != ctx.me
        await ctx.send("Dear singular message sent here in the next 15 seconds, you will be ~~f\*cked~~phucked")
        try:
            msg = await self.client.wait_for('message', check=check)
        except asyncio.TimeoutError:
            return await ctx.send('Took too long.')
        msg = msg.content
        fucksgiven = msg.split(" ")
        list(fucksgiven)
        random.shuffle(fucksgiven)
        my_ass = ""
        for i in fucksgiven:
            my_ass += ('{} ').format(i)

        my_ass = my_ass.lower()
        my_ass = my_ass.replace(".", "B") 
        my_ass = my_ass.replace("s", "sus")
        my_ass = my_ass.replace("a", "nusa")
        my_ass = my_ass.replace("l", "lusa")
        my_ass = my_ass.replace("f", "fu")
        my_ass = my_ass.replace("ni", "ninn")
        my_ass = my_ass.replace("m", "mul")




        await ctx.send(f"{my_ass}")
        await ctx.send("**phucked**")

    @commands.command(name="throw")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def throw(self, ctx, member: discord.Member = None):
        if member:
            embed=discord.Embed(title="Setting: Cafe", description=f"{ctx.author.name} is sitting at a table in a busy cafe.", color=discord.Color.red())
            embed.add_field(name=f"Out of pure anger, *{ctx.author.name}* throws a mug at *{member.name}*", value=f"The mug shatters into a million pieces, leaving *{member.name}* with injuries, the hot beverage burning their body.", inline=False)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Setting: Cafe", description=f"{ctx.author.name} is sitting at a table in a busy cafe, visibly frustrated at something unknown.", color=discord.Color.red())
            embed.add_field(name=f"Out of pure frustration and anger, *{ctx.author.name}* throws a mug at A POOR MINIMUM WAGE WORKER", value=f"The mug shatters into a million pieces, leaving them with injuries. The employee walks out of the building crying. YOU'RE SUPPOSED TO PING SOMEONE YOU MONSTER! LOOK WHAT YOU DID!", inline=False)
            await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def fuck(self, ctx,*, argument = None):
        if argument == None:
            await ctx.send(f"{ctx.author.name} fucked a mug. Why? Because they wanted to.")
        elif argument == "you":
            await ctx.send("Fuck you too")
        else:
            await ctx.send(f"A mug is magically running to screw {str(argument)}")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gay(self,ctx,*, member: discord.Member = None):
        if member:
            await ctx.send("creating trash... gimme a second")
            async with ctx.typing():
                subprocess.run("cd /home/admin/commandline_meme_generator && mkmeme \"{} be like\" -i 'https://a.pomf.cat/qtmybm.png' -p ',200' -o output.jpg".format(member.name),shell=True)
                await ctx.send(file=discord.File(r'/home/admin/commandline_meme_generator/output.jpg'))
                subprocess.run(r"rm /home/admin/commandline_meme_generator/output.jpg", shell=True)
        else:
            await ctx.send("https://a.pomf.cat/qtmybm.png")



    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def say(self,ctx,*,arg=None):
        # Satan please forgive me this was absolutely neccessary to prevent abuse.
        with open('badwords.txt') as file:
            file = file.read().split()
        for bad_words in file:
            if bad_words in arg.lower():
                return
        if bad_words not in arg.lower():
            embed=discord.Embed(color=discord.Color.blue())
            embed.add_field(name=f"{ctx.author.name}:", value=f"{arg}", inline=False)
            await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def blart(self,ctx):
        await ctx.message.add_reaction('<:psychofunny:859278377651404810>')
        await ctx.reply("https://media.discordapp.net/attachments/875508257924448317/902006682606002307/oh_my_god_pleas_help.PNG?width=280&height=468")
    @commands.command(aliases=["milk"])
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cum(self,ctx):
        await ctx.send("https://i.ibb.co/sRTfS4V/image.jpg")
    
    @commands.command()
    @commands.cooldown(1,10,commands.BucketType.user)
    async def toothbrush(self,ctx):
        await ctx.send("I'm shoving this down your throat \n https://i.ibb.co/T2rNSsz/image.png")
    @commands.command()
    @commands.cooldown(1, 10,commands.BucketType.user)
    async def drink(self,ctx):
        embed=discord.Embed(title="Setting: Cafe", description=f"{ctx.author.name} is sitting at a table in a busy cafe.", color=discord.Color.green())
        embed.add_field(name="You drink some tea from a mug", value=f"{ctx.author.name} feels refreshed and ready to continue on with their day. Satisfied with the experience, {ctx.author.name} leaves the cafe.", inline=False)
        await ctx.send(embed=embed)


    @commands.command(name="r-meme", aliases=["redditmeme"])
    async def r_meme(self,ctx):
        await ctx.reply("Fetching trash from r/memes. I don't know why I added this...")
        reddit = praw.Reddit(
            client_id="add this yourself",
            client_secret="add this yourself",
            password=f"{os.getenv('REDDIT_PASSWORD')}", # Create a new variable like we did with DISCORD_TOKEN
            user_agent="Add whatever. Doesn't matter",
            username="username that aligns with the password",
        )
        sub_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 99)
        for i in range(0, post_to_pick):
            submission = next(x for x in sub_submissions if not x.stickied)
        e = discord.Embed(title=f'It\'s surprising that I did no drugs making this command that grabs stuff from reddit', description=f'{submission.title}', color=discord.Color.blue())
        await ctx.send(f"\n {submission.url}")
def setup(client):
    client.add_cog(fun(client))
