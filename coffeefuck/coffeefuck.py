from discord.ext import commands
from discord.utils import find
from dotenv import load_dotenv
import os
import random
import discord
from discord.ext import tasks
load_dotenv();
from cogwatch import Watcher
from discord_together import DiscordTogether
from discord.ext.prettyhelp import DefaultMenu, PrettyHelp
client = commands.Bot(
    command_prefix="mug ",
    allowed_mentions=discord.AllowedMentions(
        users=False,         # Whether to ping individual user @mentions
        everyone=False,      # Whether to ping @everyone or @here mentions
        roles=False,         # Whether to ping role @mentions
        replied_user=False,  # Whether to ping on replies to messages
    ),
)
menu = DefaultMenu(
    remove=":discord:743511195197374563",
    active_time=5,
)
client.help_command = PrettyHelp(
    menu=menu
)
@client.event
async def on_ready():
    client.togetherControl = await DiscordTogether(os.getenv("DISCORD_TOKEN"))
    print("Bot ready")
    watcher = Watcher(client, path="commands", preload=True)
    await watcher.start()
    await statustask.start(client)
@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello **{}**! If you did not add me at your own will, it is your human right to remove me. If otherwise, fuck around with this. My prefix is `mug ` and an example would be `mug help`'.format(guild.name))
@commands.cooldown(1, 10, commands.BucketType.user)
@client.command()
async def party(ctx, arg=None):
    if arg == None:
        await ctx.send("We have `youtube`, `chess`, and `fishing`",delete_after=1)
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, f'{arg}')
    await ctx.send(f"Click the blue link!\n{link}")
@tasks.loop(seconds=15.0)
async def statustask(client):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'Your Mom {str(len(client.guilds))}'))
# loads the bot token from .env
client.run(os.getenv('DISCORD_TOKEN'))
