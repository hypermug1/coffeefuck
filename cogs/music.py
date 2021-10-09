import discord
from discord.ext import commands
import random
import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial,wraps
import youtube_dl
from youtube_dl import YoutubeDL

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'skip_download' : True,
    'extractaudio': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': False,
    'no_warnings': False,
    'cookiefile': 'youtube_cookie.txt',
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # ipv6 addresses cause issues sometimes
}

ffmpegopts = {
    'before_options': '-nostdin -seekable 1 -reconnect 1 -reconnect_streamed 1 -fflags flush_packets',
    # basic stuff like removing video and subtitles, then giving a volume boost
    'options': '-vn -dn -sn -filter:a "volume=3dB"'
}

ytdl = YoutubeDL(ytdlopts)

errcolor=discord.Colour.from_rgb(251,0,0)
class VoiceConnectionError(commands.CommandError):
    """Custom Exception class for connection errors."""


class InvalidVoiceChannel(VoiceConnectionError):
    """Exception for cases of invalid Voice Channels."""


class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')
        self.duration = data.get('duration')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        """Allows us to access attributes similar to a dict.
        This is only useful when you are NOT downloading.
        """
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False,timestamp:str='0'):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]


        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title'], 'duration':data['duration'],'timestamp':timestamp}

        return cls(discord.FFmpegPCMAudio(source,before_options =f"{ffmpegopts['before_options']} -ss {timestamp}",options = ffmpegopts['options']), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop,):
        """Used for preparing a stream, instead of downloading.
        Since Youtube Streaming links expire."""
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        new_data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(new_data['url'],
        before_options=f"{ffmpegopts['before_options']} -ss {data['timestamp']}",options=ffmpegopts['options']), data=new_data,requester=requester)


class MusicPlayer:
    """A class which is assigned to each guild using the bot for Music.
    This class implements a queue and loop, which allows for different guilds to listen to different playlists
    simultaneously.
    When the bot disconnects from the Voice it's instance will be destroyed.
    """

    __slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current', 'np', 'volume','repeat','queueitem','msgswitch')

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog

        self.queue = asyncio.Queue()
        self.next = asyncio.Event()
        self.repeat=None
        self.np = None  # Now playing message
        self.volume = 1
        self.current = None
        self.queueitem = None
        self.msgswitch = False
        ctx.bot.loop.create_task(self.player_loop())


    def trackcalls(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          wrapper.has_been_called = True
          return func(*args, **kwargs)
      wrapper.has_been_called = False
      return wrapper

    @trackcalls
    def repeat_state(self,ctx):
      checkstate={
        "One": lambda : (self.queue.put_nowait(self.queueitem),self.queue._queue.rotate(1-self.queue.qsize())),
        "Queue": lambda: self.queue.put_nowait(self.queueitem)
      }
      func = checkstate.get(self.repeat,lambda : '')
      try:
        func()
      except Exception:
        pass
      return self.bot.loop.call_soon_threadsafe(self.next.set)


    async def player_loop(self):
        """Our main player loop."""
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            self.next.clear()
            try:
                # Wait for the next song. If we timeout cancel the player and disconnect...
                async with timeout(900):  # 15 minutes...
                  source = await self.queue.get()
                  self.queueitem = source
            except asyncio.TimeoutError:
                return self.destroy(self._guild)

            if not isinstance(source, YTDLSource):
                # Source was probably a stream (not downloaded)
                # So we should regather to prevent stream expiration
                try:
                    source = await YTDLSource.regather_stream(source, loop=self.bot.loop)
                except Exception as e:
                    await self._channel.send(f'There was an error processing your song.\n'
                                             f'```css\n[{e}]\n```')
                    continue

            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(source, after=lambda _: self.repeat_state(self))

            if not self.msgswitch:
              embed = discord.Embed(title="Now playing", description=f"[{source.title}]({source.web_url}) [{source.requester.mention}]", color=discord.Color.magenta())
              self.np = await self._channel.send(embed=embed)
            await self.next.wait()
            # Make sure the FFmpeg process is cleaned up.
            # try:
            source.cleanup()
            # except ValueError:
              # pass
            self.current = None
    def destroy(self, guild):
        """Disconnect and cleanup the player."""
        return self.bot.loop.create_task(self._cog.cleanup(guild))


class music(commands.Cog):
    """Music related commands."""

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    def format_time(self,seconds):
      hour = seconds // 3600
      seconds %= 3600
      minutes = seconds // 60
      seconds %= 60
      if hour > 0:
          duration = "%dh %02dm %02ds" % (hour, minutes, seconds)
      else:
          duration = "%02dm %02ds" % (minutes, seconds)
      return duration

    async def cleanup(self, guild):
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass

        try:
            del self.players[guild.id]
        except KeyError:
            pass

    async def __local_check(self, ctx):
        """A local check which applies to all commands in this cog."""
        if not ctx.guild:
            raise commands.NoPrivateMessage
        return True

    async def __error(self, ctx, error):
        """A local error handler for all errors arising from commands in this cog."""
        if isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.send('This command can not be used in Private Messages.')
            except discord.HTTPException:
                pass
        elif isinstance(error, InvalidVoiceChannel):
            await ctx.send('Error connecting to Voice Channel. '
                           'Give me a valid voice channel or i\'ll fuck you up the ass with a pitchfork')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    def get_player(self, ctx):
        """Retrieve the guild player, or generate one."""
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    @commands.command(name='join', aliases=['connect', 'j'], description="connects to voice")
    async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
        """
        Connects the bot to the voice chat and stuff. You can specify a voice channel or alternatively have it join the same one as you.
        """
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                embed = discord.Embed(title="", description="WHAT CHANNEL? HAVE YOU TRIED `join` WHILE CONNECTED TO A VOICE CHANNEL YOU TWIT?.", color=discord.Color.magenta())
                await ctx.send(embed=embed)
                raise InvalidVoiceChannel('GIMME VALID CHANNEL OR JOIN A CHANNEL DIMWIT')

        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Moving to channel: <{channel}> timed out.')
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Connecting to channel: <{channel}> timed out.')
        if (random.randint(0, 1) == 0):
            await ctx.message.add_reaction('<:psychofunny:859278377651404810>')
        await ctx.message.add_reaction('👍')

    @commands.command(name='play', aliases=['sing','p','pl'], description="streams music")
    async def play_(self, ctx, *, search: str=None):
        """Request audio"""
        await ctx.trigger_typing()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)
        elif not ctx.author.voice or vc.channel.id!=ctx.author.voice.channel.id:
          return await ctx.send(embed=discord.Embed(title='',description=f"**{ctx.author}**, you are not connected to proper voice channel",color=discord.Colour.from_rgb(251,0,0)))
        elif vc.is_playing() and search==None:
          return await ctx.invoke(self.pause_)

        player = self.get_player(ctx)

        # If download is False, source will be a dict which will be used later to regather the stream.
        # If download is True, source will be a discord.FFmpegPCMAudio with a VolumeTransformer.
        source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)
        if not player.msgswitch:
          await ctx.send(f"Queued **{source['title']}**")
        await player.queue.put(source)

    @commands.command(name='pause',aliases = ['pa','ps'], description="pauses music")
    async def pause_(self, ctx):
        """Pause the currently playing song."""
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            embed = discord.Embed(title="", description="*oh sorry lemme just pause that silence for you master*", color=discord.Color.magenta())
            return await ctx.send(embed=embed)
        elif vc.is_paused():
            return

        vc.pause()
        await ctx.send("Paused ⏸️")

    @commands.command(name='resume',aliases=['res','unpause','r'], description="resumes music")
    async def resume_(self, ctx):
        """Resume something that is paused. Duh."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="i am not connection, bitch", color=discord.Color.magenta())
            return await ctx.send(embed=embed)
        elif not vc.is_paused():
            return

        vc.resume()
        await ctx.send("Resuming ▶️")

    @commands.command(name='skip',aliases=['sk'],description="skips to next song in queue")
    async def skip_(self, ctx):
        """Skip the song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I am not connection, bitch", color=discord.Color.magenta())
            return await ctx.send(embed=embed)

        if vc.is_paused():
            pass
        elif not vc.is_playing():
            return

        vc.stop()
        await ctx.message.add_reaction('😏')

    @commands.command(name='remove', aliases=['rm', 'rem'], description="removes specified song from queue")
    async def remove_(self, ctx, pos : int=None):
        """Removes specified song from queue"""

        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="Connect me first father", color=discord.Color.magenta())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if pos == None:
            player.queue._queue.pop()
        else:
            try:
                s = player.queue._queue[pos-1]
                del player.queue._queue[pos-1]
                embed = discord.Embed(title="", description=f"Removed [{s['title']}]({s['webpage_url']}) [{s['requester'].mention}]", color=discord.Color.magenta())
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(title="", description=f'Could not find a track for "{pos}"', color=discord.Color.dark_blue())
                await ctx.send(embed=embed)

    @commands.command(name='clear', aliases=['clr', 'cl', 'cr'], description="clears entire queue")
    async def clear_(self, ctx):
        """Deletes entire queue of upcoming songs."""

        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="add me first, you fucking submissive as hell and breedable fucking gamer boy uwu x3", color=discord.Color.magenta())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        player.queue._queue.clear()
        await ctx.send('**Cleared**')

    @commands.command(name='queue', aliases=['q', 'playlist', 'que'], description="shows the queue")
    async def queue_info(self, ctx):
        """Retrieve a basic queue of upcoming songs."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="Queue", description="Longer than my list of privacy rights under the US government", color=discord.Color.magenta())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if player.queue.empty() and vc.source:
          return await ctx.invoke(self.now_playing_)
        if player.queue.empty():
            embed = discord.Embed(title="", description="Queue is empty", color=discord.Color.magenta())
            return await ctx.send(embed=embed)

        seconds = vc.source.duration % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            duration = "%dh %02dm %02ds" % (hour, minutes, seconds)
        else:
            duration = "%02dm %02ds" % (minutes, seconds)

        # Grabs the songs in the queue...
        upcoming = list(itertools.islice(player.queue._queue, 0, int(len(player.queue._queue))))
        fmt = '\n'.join(f"`{index + 1}.` __**[{_['title']}]({_['webpage_url']})**__ | ` {self.format_time(_['duration'])}` Requested by: {_['requester'].mention}\n" for index,_ in enumerate(upcoming))
        fmt = f"\n__**Now Playing**__:\n__**[{vc.source.title}]({vc.source.web_url})**__ | ` {duration}` Requested by: {vc.source.requester.mention}\n\n__**Up Next:**__\n" + fmt
        embed = discord.Embed(title=f'Queue for {ctx.guild.name}', description=fmt, color=discord.Color.magenta())
        embed.add_field(name="Entries",value=len(upcoming),inline=True)
        embed.add_field(name="Total Duration", value=self.format_time(sum(_['duration']for _ in upcoming)) , inline=True)
        embed.add_field(name="Repeat Status",value=player.repeat,inline=True)
        embed.set_footer(text=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(name='np', aliases=['song', 'current', 'currentsong', 'playing'], description="shows the current playing song")
    async def now_playing_(self, ctx):
        """Display information about the currently playing song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="Currently playing", description="The \"add me to the fricking voice channel\" song", color=discord.Color.magenta())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if not player.current:
            embed = discord.Embed(title="Currently playing", description="Your dad", color=discord.Color.magenta())
            return await ctx.send(embed=embed)

        seconds = vc.source.duration % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            duration = "%dh %02dm %02ds" % (hour, minutes, seconds)
        else:
            duration = "%02dm %02ds" % (minutes, seconds)

        embed = discord.Embed(title="", description=f"[{vc.source.title}]({vc.source.web_url}) [{vc.source.requester.mention}] | `{duration}`", color=discord.Color.magenta())
        embed.set_author(icon_url=self.bot.user.avatar_url, name=f"Now Playing 🎶")
        await ctx.send(embed=embed)

    @commands.command(name='volume', aliases=['vol', 'v'], description="changes Kermit's volume")
    async def change_volume(self, ctx, *, vol: float=None):
        """Change the player volume.
        Parameters
        ------------
        Volume. Set it. 300 is maximum.
        """
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="Volume set to: ADD ME TO THE FRICKING CHANNEL", color=discord.Color.magenta())
            return await ctx.send(embed=embed)

        if not vol:
            embed = discord.Embed(title="", description=f"🔊 **{(vc.source.volume)*100}%**", color=discord.Color.magenta())
            return await ctx.send(embed=embed)

        if not 0 < vol < 301:
            embed = discord.Embed(title="", description="Please enter a value between 1 and 300", color=discord.Color.magenta())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)

        if vc.source:
            vc.source.volume = vol / 100

        player.volume = vol / 100
        embed = discord.Embed(title="", description=f'**`{ctx.author}`** set the volume to **{vol}%**', color=discord.Color.magenta())
        await ctx.send(embed=embed)
    @commands.command(name='extremebassboost', aliases=['bassboost', 'loud'], description="changes Kermit's volume")
    async def bassboost(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="Volume set to: ADD ME TO THE FRICKING CHANNEL", color=discord.Color.magenta())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)

        if vc.source:
            vc.source.volume = 10000000

        player.volume = 10000000 / 100
        self.volume = 500
        embed = discord.Embed(title="", description="FUCK :volcano: 🔊 ", color=discord.Color.magenta())
        await ctx.send(embed=embed)

    @commands.command(name='leave', aliases=["stop", "dc", "disconnect", "bye",'fuckoff'], description="stops music and disconnects from voice")
    async def leave_(self, ctx):
        """Stop the currently playing song and destroy the player.
        !Warning!
            This will destroy the player assigned to your guild, also deleting any queued songs and settings.
        """
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not in a voice channel. Do you want me to leave/stop/disconnect the universe?", color=discord.Color.magenta())
            return await ctx.send(embed=embed)
        elif vc.is_connected() and (not ctx.author.voice or vc.channel.id!=ctx.author.voice.channel.id):
          return await ctx.send(embed=discord.Embed(title='',description=f"**{ctx.author}**, you are not connected to proper voice channel",color=discord.Colour.from_rgb(251,0,0)))

        if (random.randint(0, 1) == 0):
            await ctx.message.add_reaction('🖕')
        await ctx.send('**I destroyed this place :volcano:**')

        await self.cleanup(ctx.guild)
    @commands.command(name="repeat", aliases=["loop","lp","rp"], description="Sets the queue or song on repeat.")
    async def repeat(self, ctx, state=None):
      """Sets the queue or song on repeat. Values: None, One/song or Queue. Default is set to None."""
      player=self.get_player(ctx)
      player.repeat={
        "None":None,
        "none":None,
        None : None,
        "Queue":"Queue",
        "queue":"Queue",
        "One":"One",
        "one":"One",
        "song":"One",
        "Song":"One"
      }.get(state,None)
      embed = discord.Embed(title="", description="Repeat is now set to **{}**".format(player.repeat),color=discord.Color.magenta())
      await ctx.send(embed = embed)
      return

    @commands.command(name="search",aliases=["sr","yt","youtube"], description="Shows top 5 search results from youtube")
    async def search(self,ctx,*,search):
      """Shows top 5 search results from youtube"""

      player = self.get_player(ctx)
      loop = player.bot.loop or asyncio.get_event_loop()
      to_run = partial(ytdl.extract_info, url=f"ytsearch5:{search}", download=False)
      data = await loop.run_in_executor(None, to_run)
      data=data['entries']
      fmtstr='\n'.join(f"`{data.index(_)+1}.` __**[{_['title']}]({_['webpage_url']})**__ | `{self.format_time(_['duration'])}`\n" for _ in data)
      embed = discord.Embed(title="**Top Search Results**", description=fmtstr,color=discord.Color.magenta())
      embed.set_footer(text=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed = embed)
      try:
        msg = await player.bot.wait_for("message",timeout=30)
        req_idx = msg.content
        req_idx = int(req_idx.strip())
        word = data[req_idx-1]['webpage_url']
        await ctx.invoke(self.play_,search=word)
      except asyncio.TimeoutError:
          await ctx.send("Sorry, you didn't reply in time!")
      except TypeError:
          await ctx.send("Wrong input")

    @commands.command(name="seek")
    async def seek_(self,ctx,time:str=None):
      player=self.get_player(ctx)
      vc = ctx.voice_client
      if not vc or not vc.is_connected():
        return await ctx.send(discord.Embed.from_dict({
          "description":"I'm not connected to a voice channel",
          "color":errcolor.value
        }))
      elif not vc.is_playing():
        return await ctx.send(discord.Embed.from_dict({
          "description":"please Resume a song to seek",
          "color":errcolor.value
        }))
      if time==None:
        return await ctx.send(embed=discord.Embed(description="Wrong timestamp",colour=discord.Colour.from_rgb(251,0,0)))
      loop = player.bot.loop or asyncio.get_event_loop()
      source = await YTDLSource.create_source(ctx,player.queueitem['webpage_url'], loop=loop, download=False,timestamp=time)
      await ctx.send(embed=discord.Embed.from_dict({
        'description': f'Seeking song to `{time}s`'if time.isdigit() else f'Seeking song to `{time}`',
        'color': discord.Colour.dark_blue().value
      }))
      player.msgswitch=True
      old_repeat=player.repeat
      player.repeat="One"
      player.queueitem=source
      await self.skip_(ctx)
      await asyncio.sleep(2)
      player.repeat=old_repeat
      player.msgswitch=False
      player.queueitem['timestamp']='0'

def setup(bot):
    bot.add_cog(music(bot))
