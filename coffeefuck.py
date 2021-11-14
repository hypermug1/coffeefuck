from discord.ext import commands
from discord.ext import fancyhelp
from dotenv import load_dotenv
import os
import random
import discord
from discord.ext import tasks
load_dotenv();
from cogwatch import Watcher
from discord_together import DiscordTogether
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
    client.togetherControl = await DiscordTogether(os.getenv("DISCORD_TOKEN"))
    print("Bot ready")
    client.help_command = fancyhelp.EmbeddedHelpCommand()
    watcher = Watcher(client, path="commands", preload=True)
    await watcher.start()
    await statustask.start(client)
@client.command()
async def party(ctx, arg=None):
    if arg == None:
        await ctx.send("We have `youtube`, `chess`, and `fishing`")
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, f'{arg}')
    await ctx.send(f"Click the blue link!\n{link}")

@tasks.loop(seconds=15.0)
async def statustask(client):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'fiddle x{str(len(client.guilds))} with the devil'))
# loads the bot token from .env
client.run(os.getenv('DISCORD_TOKEN'))
