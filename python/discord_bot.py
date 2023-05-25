import discord
from discord.ext import commands
import word_list
import os
import youtube_dl
from discord import permissions

# from musicDiscord import *


activity = discord.Activity(
    name="coolseniorproject.me", type=discord.ActivityType.watching
)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents, activity=activity)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # messasgeSplit = message.content.split()
    # for word in messasgeSplit:
    #     if word in word_list.word_list:
    #         print(word + " is in the list so kicked")
    #         await message.author.kick()


@client.event
async def on_message_delete(message):
    if message.author == client.user:
        await message.channel.send(message.content + ":skull:")
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


client.run("MTExMTM3NDY3MTU0NDM0MDU1Mg.Gp7VwD.G7MYgBXvuCnS4Y9EmzlylkEgKsb5rFzmp6S224")


"""

bot_Command = commands.Bot(command_Prefix = "$")

bot.add_cog(musicDiscord(bot_Command))

bot_Command.run(MTExMTM3NDY3MTU0NDM0MDU1Mg.Gp7VwD.G7MYgBXvuCnS4Y9EmzlylkEgKsb5rFzmp6S224)






"""
