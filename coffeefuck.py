from discord.ext import commands
from dotenv import load_dotenv
import os
import random
import discord
from discord.ext import tasks
load_dotenv();
from cogwatch import Watcher
client = commands.Bot(
    command_prefix="mug ",
    allowed_mentions=discord.AllowedMentions(
        users=False,         # Whether to ping individual user @mentions
        everyone=False,      # Whether to ping @everyone or @here mentions
        roles=False,         # Whether to ping role @mentions
        replied_user=False,  # Whether to ping on replies to messages
    ),
)
@client.event
async def on_ready():
    print("Bot ready.")

    watcher = Watcher(client, path="cogs", preload=True)
    await watcher.start()
    await statustask.start(client)
class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.blurple(), description=' ')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

client.help_command = MyHelpCommand()
@tasks.loop(seconds=10.0)
async def statustask(client):
    statuses = ["rats fighting over food", "the leaves fall" , "pigeons", "for [mug help]", "you :)", "flowers grow", "seasons change", "the skies", "the rain fall", "a show"]
    newstatus = random.choice(statuses)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{newstatus}"))

#loads the "discord.com/developers" bot token in .env and starts the bot.
client.run(os.getenv('TOKEN'))
