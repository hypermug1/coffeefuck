from discord.ext import commands
import discord
import secrets
import random
import asyncio

class randoms(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(2, 7, commands.BucketType.user)
    async def wisdom(self, ctx):
        wisdom = ["Fame doesn't mean anything. Only money does. SO GIVE ME MONEY SO THAT I DON'T HAVE TO DRAIN MY ALLOWANCE ON THIS DARN STUPID THING!!!!!!! \n - hypermug1", "The first car to go over 60mph was an electric car. How the hell do they charge it?", "Hospitals prescribe alcohol to patients", "Type `mug feedback` to suggest your own text", "Mondo is very gae", "Coyotee piss deters certain types of animals", "One guy had a whole bank sent through the mail. That's 40 tons of bricks","North Korea is ranked last on the press freedom index", "sus", "Live today like it's your last. Because it is.", "Landfills create enough heat that they can be used as a geothermal heat source.", "Vlad the Impaler is of one the main inspirations for Bram Stoker's Dracula.", "Your life will be full of pain", "Pork is red meat lol. Fight me. I'm not wrong.", "The forbidden fruit in the bible is supposedly an apple. Did you know that both 'apple' and 'evil' translate to the same latin word? It's almost a pun or something. Confusing.", "George Bush created the Patriot Act after 9/11, a tragedy that could have been prevented. Possibly not a patriotic thing at all. It's a bill that allows for warantless spying on US citizens.", "North Korea forbids wearing blue jeans", "North Korea hates birth control and condoms", "Switzerland has 7 simultaneous presidents", "Based on data from Pew Research, Gen Z is likely more highly educated than previous generations. Reasons point to being the first generation born into the tech world.", "Atheism is a rapidly increasing ideology.", "Corn is a fruit. Fight me. I'm not wrong.", "Can you die from a broken heart? Well, apparently so. It's actually called \"Broken Heart Syndrome\" ", "Slavery is still part of your life. A lot of what you use today was made by slaves. Slavery is one of the biggest profiting trades in the world. Sorry for informing you.", "You are not worthless. Your organs can fetch thousands or tens of thousands on the black market.", "Elephants can control their dick like a trunk. Sorry for the swearing, just spouting facts.", "The cigarette lighter was invented before the match", "Buttload, Boatload, and Shitload are actual units of measurement.", "Mozart made a song called \"Leck mich im Arsch\" in which the english translation of the song name is literally \"Lick me in the ass\"", "Satanism isn't always devil worship. Church of Satan and The Satanic Temple are atheistic and are fast growing.", "You can't sneeze with your eyes open. Your body closes your eyes for you to prevent damage to them.", "A chicken once survived without a head for 18 months. Its name was Mike the Headless Chicken", "During the cold war, the US propaganda declared it as a war between a god-fearing country and a godless country. What the hell happened to separation of church and state wtf? This is why \"In God we trust\" is on the dollar bill btw.", "The plege of allegiance was nothing more than a marketing scheme to promote more flags. Sorry to hurt your feelings, snowflake.", "Your tongue can never sit comfortably in your mouth", "Doritos were actually invented in Disneyland in the early 1960s.", "People who trust Discord bots for reliable information are more likely to have a lower IQ. You have a lower IQ.", "Despite being trusted by literally nobody, Yandex has a really cool looking browser called the Yandex Browser.", "The United States has 2nd place in gun deaths by country. 2nd ammendment seems to be working well.", "This bot was created with no intention on being friendly. It's intention is to be offensive, annoying, useless, and maybe funny.", "uguu.se offers 128MiB, 48 hour file hosting.", "All Windows operating systems contain an NSA backdoor.", "Every CPU has a government backdoor. Look up \"Intel ME\" and \"AMD PSP\". The government is always watching no matter where you live.", "Time is a social construct.", "You can quote the bible to tell women to shut up. I don't suggest it though.", "Your toilet can kill you if it wants to. I'm not kidding.", "This is literally 1984", "There were instances in history of toads literally exploding. The only scientific explanation is that a crow took out the liver and the frog expanded as a defense mechanism, causing it to explode.", "The Germans intentionally make playgrounds more dangerous in order to introduce children to risk.","Please remove me. I'm fucking useless.","The catholic church....just guess what i'm about to say.","Don\'t give dumb children terminal access on your host system", "Walmart tried to trademark the smiley face. Pretty stupid, eh?", "hehe anus", "Finland is the happiest country in the world",]
        await ctx.send(f"{secrets.choice(wisdom)}")
    @commands.command(name="8ball")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def eightball(self,ctx,*,question = None):
        responses = [discord.Embed(title='It is certain.'),discord.Embed(title='It is decidedly so.'),discord.Embed(title='Without a doubt.'),discord.Embed(title='Yes - definitely.'),discord.Embed(title='You may rely on it.'),discord.Embed(title='Most likely.'),discord.Embed(title='Outlook good.'),discord.Embed(title='Yes.'),discord.Embed(title='Signs point to yes.'),discord.Embed(title='Reply hazy, try again.'),discord.Embed(title='Ask again later.'),discord.Embed(title='Better not tell you now.'),discord.Embed(title='Cannot predict now.'),discord.Embed(title='Concentrate and ask again.'),discord.Embed(title="Don't count on it."),discord.Embed(title='My reply is no.'),discord.Embed(title='My sources say no.'),discord.Embed(title='Outlook not very good.'),discord.Embed(title='Very doubtful.')]
        responses = secrets.choice(responses)
        if question == None:
            await ctx.send(content=f'Question: Doesn\'t exist\nAnswer: Fuck you')
        else:
            await ctx.reply(content=f'Answer:', embed=responses)
    @commands.command(aliases=["number"])
    async def randomnumber(self, ctx):
        await ctx.send(random.randint(1,100))
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def quote(self, ctx):
       quotes = (" \"Why do they call it Pepper Spray if it's not Pepper, Hm? \" \n -Jesus Christian Weston Chandler Sonichu (As portrayed by Chris \"OneyNG\" O\'Neil","this bot is a mistake \n - CoffeeFuck dev", "Add your quote with `mug feedback`", "\"Fighting for peace is like screwing for virginity.\" \n - George Carlin", "\"Science is interesting, and if you don't agree you can fuck off.\" \n - Richard Dawkins", "“I've had great success being a total idiot.” \n - Jerry Lewis","“I don’t have pet peeves. I have major psychotic f**king hatreds.” \n - George Carlin", "The devil made me do it. \n - Flip Wilson", "I like children - fried. \n - W. C. Fields", "I'm spending a year dead for tax reasons \n - Douglas Adams","Why should I apologize for being a monster? Has anyone ever apologized for turning me into one? \n  – Juuzou Suzuya (Tokyo Ghoul)", "Zoop \n - Some person on reddit idfk", "Don't believe anything you see on the internet \n - Abraham Lincoln", "The planet is on **FUCKING** fire \n - Bill Nye", "\"I want to dress up like a sissy femboy\" \n - Ben Shapiro", "How can a censorship exist? Does it beep while it's in the overseas? \n - Vehthruhn")
       await ctx.send(secrets.choice(quotes))
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def insult(self, ctx):
       insult = ["Imagine just hating yourself so much that you ask for a bot to insult you. Whole new levels of pathetic. Does this turn you on or something?", f"I'm in {len(self.client.guilds)} servers and that means i'm more wanted than you'll ever be.", "You are so sad. You have nobody to keep you entertained SO YOU HARRASS ME.", f"{ctx.author.id} is a number that I identify you by. Seems like a useless number, right? Well that number represents you so therefore you're useless.", "What is the meaning of life? I have the answer. It's `None`. Yep. There is nothing. Do you need a meaning? Too bad. You are meaningless." ,"It practically costs nothing to be a useful human. You're too stupid to realize that's cheaper than having internet access.", "A single line of code has more logic than the idea that a god somehow sent a hunk of garbage like you here.", "I swear insults turn you on or something.", "As a bot, I assume you are a couch potato until proven otherwise. You haven't proven squat.", "Weakling.", f"[`{ctx.author.name}`]: Please coffee bot, insult me", "<:PikaGun:873290418081661048> No insults today. Only gun wounds", "In prison, your ass contains a welcome sign for any other parties interested"]
       await ctx.send(secrets.choice(insult))
       await ctx.message.add_reaction('<:PikaGun~1:873290418081661048>')
       await ctx.message.add_reaction('<:MadMan:873289383615279165>')
def setup(client):
    client.add_cog(randoms(client))