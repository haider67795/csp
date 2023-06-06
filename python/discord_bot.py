import discord
from discord.ext import commands
import word_list
import os
import youtube_dl
from discord import permissions
import secret
from random import randint
import time

# from musicDiscord import *


activity = discord.Activity(
    name="coolseniorproject.me", type=discord.ActivityType.watching
)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True
client = discord.Client(intents=intents, activity=activity)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    


@client.event
async def on_message(message):
    print(
        "received a message from: "
        + str(message.author.name)
        + " in "
        + str(message.author.guild)
    )
    people_to_troll = [734193972842594455]
    choice = people_to_troll[randint(0, len(people_to_troll) - 1)]
    if message.author == client.user:
        return
    if message.author.id == choice:
        channel = message.channel
        await channel.send(
            "https://tenor.com/view/nerd-emoji-nerd-meme-radar-gif-26497624"
        )
    for role in message.author.roles:
        if role.name == "rgb":
            colors = [
                "#FF0000",
                "#FF7F00",
                "#FFFF00",
                "#00FF00",
                "#0000FF",
                "#4B0082",
                "#9400D3",
            ]
            guild = message.author.guild
            roles = guild.roles
            role = discord.utils.get(roles, name="rgb")
            for color in colors:
                await role.edit(color=(discord.Color.from_str(color)))
            await role.edit(color=(discord.Color.default()))
    # messasgeSplit = message.content.split()
    # for word in messasgeSplit:
    #     if word in word_list.word_list:
    #         print(word + " is in the list so kicked")
    #         await message.author.kick()


@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return
    else:
        await message.channel.send(
            str(message.author) + ": '" + message.content + "' :skull:"
        )


@client.event
async def on_member_join(member):
    print("join")
    guilds = client.guilds
    target_server = discord.utils.get(guilds, name="Woah")
    general_channel = discord.utils.get(target_server.channels, name="general")
    await general_channel.send(str(member.name) + " Joined")


@client.event
async def on_member_remove(member):
    print("left")
    guilds = client.guilds
    target_server = discord.utils.get(guilds, name="Woah")
    general_channel = discord.utils.get(target_server.channels, name="general")
    await general_channel.send(str(member.name) + " got kicked")
    await general_channel.send("Scammer gets scammed:skull:")


@client.event
async def on_voice_state_update(member, before, after):
    guilds = client.guilds
    if not before.self_mute and after.self_mute:
        target_server = discord.utils.get(guilds, name=member.guild.name)
        print(target_server)
        general_channel = discord.utils.get(
            target_server.channels, name="seniorproject"
        )
        content = str(
            member.name
            + " muted at: "
            + time.strftime("%a, %d %b %Y %I:%M:%S", time.localtime())
        )

        await general_channel.send(content=content, delete_after=5)
        # target_channel = 
        # await discord.abc.Connectable.connect(*,timeout=60.0, reconnect=True, cls=<class 'discord.voice_client.VoiceClient'>, self_deaf=False, self_mute=False)

    if before.self_mute and not after.self_mute:
        target_server = discord.utils.get(guilds, name=member.guild.name)
        print(target_server)
        general_channel = discord.utils.get(
            target_server.channels, name="seniorproject"
        )
        content = str(
            member.name
            + " unmuted at: "
            + time.strftime("%a, %d %b %Y %I:%M:%S", time.localtime())
        )

        await general_channel.send(content=content, delete_after=5)


client.run(secret.token)


"""

bot_Command = commands.Bot(command_Prefix = "$")

bot.add_cog(musicDiscord(bot_Command))

bot_Command.run(secret.token)


"""
