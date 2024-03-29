# bot.py
import os
import random
import time
import asyncio
import wow_audio

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

joined = 0
messages = 0

client = discord.Client()
commands_txt = ["wow", "scubaba", "99"]
exe = "/usr/bin/ffmpeg"     # If you want to run the bot on a Linux machine
# exe_windows = "C:/ffmpeg/ffmpeg-20200426-1128aa8-win64-static/bin/ffmpeg.exe" # If you want to run the bot on a Windows machine

@bot.command(name='commands')
async def commands(ctx):
    response = ""
    for command in commands_txt:
        response += '{} \n '.format(command)
    await ctx.send(response)


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    user = ctx.message.author
    brooklyn_99_quotes = [
        'I\'m the human form of the ðŸ’¯ emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='hello')
async def hello(ctx):
    await ctx.channel.send("Hi")


@bot.command(
    name='wow',
    description='wow',
    pass_context=True,
    help='wow'
)
async def wow(context):
    # grab the user who sent the command
    user = context.author
    voice_channel = context.author.voice.channel
    # only play music if user is in a voice channel
    if voice_channel is not None:
        # grab user's voice channel
        # create StreamPlayer
        vc = await voice_channel.connect()
        try:
            vc.play(discord.FFmpegPCMAudio(executable=exe, source=random.choice(wow_audio.wow_list)))
            vc.is_playing()
            while vc.is_playing():
                await asyncio.sleep(1)
            # disconnect after the player has finished
            vc.stop()
            await vc.disconnect()
        except:
            await vc.disconnect()
    else:
        await context.send('User is not in a channel.')


@bot.command(
    name='scubaba',
    description='scubaba',
    pass_context=True,
    help='scubaba'
)
async def scubaba(context):
    # grab the user who sent the command
    user = context.message.author
    voice_channel = user.voice.channel
    channel = None
    # only play music if user is in a voice channel
    if voice_channel is not None:
        # grab user's voice channel
        # create StreamPlayer
        vc = await user.voice.channel.connect()
        try:
            vc.play(discord.FFmpegPCMAudio(executable=exe, source=random.choice(wow_audio.scubaba)))
            vc.is_playing()
            while vc.is_playing():
                await asyncio.sleep(1)
            # disconnect after the player has finished
            vc.stop()
            await vc.disconnect()
        except:
            await vc.disconnect()
    else:
        await context.send('User is not in a channel.')


@bot.command(
    name='hehe',
    description='hehe',
    pass_context=True,
    help='hehe'
)
async def hehe(context):
    # grab the user who sent the command
    user = context.message.author
    voice_channel = user.voice.channel
    channel = None
    # only play music if user is in a voice channel
    if voice_channel is not None:
        # grab user's voice channel
        # create StreamPlayer
        vc = await user.voice.channel.connect()
        try:
            vc.play(discord.FFmpegPCMAudio(executable=exe, source=random.choice(wow_audio.ole_wedel)))
            vc.is_playing()
            while vc.is_playing():
                await asyncio.sleep(1)
            # disconnect after the player has finished
            vc.stop()
            await vc.disconnect()
        except:
            await vc.disconnect()
    else:
        await context.send('User is not in a channel.')


@bot.command(
    name='wololo',
    description='wololo',
    pass_context=True,
    help='wololo'
)
async def wololo(context):
    # grab the user who sent the command
    user = context.author
    voice_channel = context.author.voice.channel
    # only play music if user is in a voice channel
    if voice_channel is not None:
        # grab user's voice channel
        # create StreamPlayer
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=exe, source=random.choice(wow_audio.wololo)))
        vc.is_playing()
        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
        await vc.disconnect()
    else:
        await context.send('User is not in a channel.')

@bot.command(
    name='sådan',
    description='sådan',
    pass_context=True,
    help='sådan'
)
async def wololo(context):
    # grab the user who sent the command
    user = context.author
    voice_channel = context.author.voice.channel
    # only play music if user is in a voice channel
    if voice_channel is not None:
        # grab user's voice channel
        # create StreamPlayer
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=exe, source=random.choice(wow_audio.saadan)))
        vc.is_playing()
        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
        await vc.disconnect()
    else:
        await context.send('User is not in a channel.')

@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message("Welcome to the server {}".format(member.mention))

bot.run(TOKEN)
