from discord.ext import commands
import discord
import random
import asyncio
import time
from discord.ext import tasks
class MiscFunction(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.cooldown(3, 10, commands.BucketType.user)
    @commands.Cog.listener()
    async def on_message(self,message):
        mention = f'<@!{self.client.user.id}>'
        if mention in message.content and message.content:
            await message.author.send('I have been pinged. My help command is `mug help` btw')

        if message.content == 'fuck you mug' or message.content == 'fuck you coffeefuck':
            await message.author.send('Fuck you too', delete_after=120)

        if message.content == 'mug':
            await message.add_reaction("😩")
            await message.reply("yes daddy? :smiling_imp:",delete_after=1000)
def setup(client):
    client.add_cog(MiscFunction(client))
