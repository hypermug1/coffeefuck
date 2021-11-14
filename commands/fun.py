from discord.ext import commands
import discord
import asyncio
import subprocess
import random
import typing
from discord_together import DiscordTogether
class fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.counter = 32
    @commands.Cog.listener()
    async def on_message(self,message):
        mention = f'<@!{self.client.user.id}>'
        if mention in message.content:
            await message.channel.send("fuck you <:psychofunny:859278377651404810>")

        if "mug go fucking die in a ditch ngl" in message.content.lower():
            await message.channel.send("no u")

    @commands.command(name="meme")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self,ctx,*,message = None):
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
        my_ass = my_ass.replace("he", "she")
        my_ass = my_ass.replace("everyone ", "nobody")
        my_ass = my_ass.replace("is", "isnt")
        my_ass = my_ass.replace("god", "satan")
        my_ass = my_ass.replace("the", "them")
        my_ass = my_ass.replace("best", "worst")
        my_ass = my_ass.replace("awesome", "awful")
        my_ass = my_ass.replace("car", "truck")
        my_ass = my_ass.replace("person", "arsonist")
        my_ass = my_ass.replace("sky", "chicken")
        my_ass = my_ass.replace("impostor", "spy")
        my_ass = my_ass.replace("fuck", "phuck")
        my_ass = my_ass.replace("no", "yes")
        my_ass = my_ass.replace("my", "his")
        my_ass = my_ass.replace("she", "he")
        my_ass = my_ass.replace("ay", "aye")
        my_ass = my_ass.replace("why", "cause")
        my_ass = my_ass.replace("e", "i")
        my_ass = my_ass.replace("e", "i")
        my_ass = my_ass.replace("e", "i")
        my_ass = my_ass.replace("i", "o")
        my_ass = my_ass.replace("o", "e")
        my_ass = my_ass.replace("y", "f")
        my_ass = my_ass.replace("g", "go")
        my_ass = my_ass.replace("a", "AAA")
        my_ass = my_ass.replace("u", "ual")



        await ctx.send(f"{my_ass}")
        await ctx.send("**phucked**")

    @commands.command(name="throw")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def throw(self, ctx, member: discord.Member = None):
        if member:
            embed=discord.Embed(color=discord.Color.blue())
            embed.add_field(name="OH SHIT", value=f"IT APPEARS **{ctx.author.name}** threw a mug at **{member.name}**! ***WHO'S PAYING FOR THE HOSPITAL BILL? FIND OUT ON THE NEXT EPISODE OF I HAVE NO IDEA.***", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"A poor coffee shop worker just got fucking murdered with a mug. This is not what you're SUPPOSED TO DO! You're supposed to PING SOMEONE IN THE COMMAND")
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def fuck(self, ctx,*, argument = None):
        if argument == None:
            await ctx.send(f"{ctx.author.name} fucked a mug. Why? Because they wanted to.")
        elif argument:
            await ctx.send(f"A mug has been sent to do unholy things to {str(argument)}")
        elif argument == "you":
            await ctx.send("Fuck you too")

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
    @commands.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def touch(self, ctx):
        self.counter += 1
        embed=discord.Embed(color=discord.Color.blue())
        embed.add_field(name="Great! FANTASTIC! ABSOLUTELY MARVELOUS!", value=f"Thanks to you annoying fricks, this already dirty mug has been touched by your filthy hands **{self.counter}** time since I have been awake.", inline=False)
        embed.set_footer(text="I slammed my head against my desk and got brain damage trying to use a database here. Eventually, I gave up and now the counter resets when the bot is updated/restarted.")
        await ctx.send(embed=embed)
    @commands.command(aliases=["milk"])
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cum(self,ctx):
        await ctx.send("https://i.ibb.co/sRTfS4V/image.jpg")
def setup(client):
    client.add_cog(fun(client))
