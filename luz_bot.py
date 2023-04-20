# -*- coding: utf-8 -*-

"""
privates tokens
"""
from tkn import key,welcome,goodbye,update # key : discord bot token // Other : Channels ID

"""
Lib for the bot
"""
import discord
from discord import *
from discord.utils import get
from discord.ext import commands
from fonction import *

default_intents = discord.Intents.default()
default_intents.members = True

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.',intents=intents)


@bot.event
async def on_ready():
    """
    Tell the dev when the bot is online
    """
    print("The bot is online")

@bot.event
async def on_member_join(member):
    """
    Greetings when a member join a guild
    """
    bienvenue: discord.TextChannel = client.get_channel(welcome)
    await bienvenue.send(content=
        f"Welcome {member.display_name} !"
    )

@bot.event
async def on_member_remove(member):
    """
    Goodbye when a member leave a guild
    """
    a_la_prochaine: discord.TextChannel = client.get_channel(goodbye)
    await a_la_prochaine.send(content=f"Goodbye {member.display_name} !")

@bot.event
async def on_disconnect():
    """
    Tell the dev when the bot is offline
    """
    print("The bot is offline")

@bot.event
async def on_member_update(before, after):
    """
    Inform the guild when a member change his name
    """
    changement: discord.TextChannel = client.get_channel(update)
    if {before.display_name} != {after.display_name}:
        await changement.send(content=f"{before.display_name} became {after.display_name} !")




filedico = {
    "!command" : 'FILE',
    "!command_2" : 'FILE_2',
}

messagesLUT = {
    "!farkdateproduction" :
        "https://www.youtube.com/channel/UC0f0m2dVJSu9TXkh23Unhhw",
    "!help" :
        """
> Luz welcomes when a new member joins the server.
> Luz says goodbye to those who leave us (sad).
> Luz warns when members change their nickname in order to recognize them.
> Luz has some really cool commands
> Luz can ask a question to start a conversation
> Luz doesn't look like that but he's a real chad, he just can't clean.
> Luz can play any game you want (even those that don't exist)
        """,
    "!command":
        "ANSWER",
    "!command_2":
        "ANSWER_2"
}


@bot.event
async def on_message(message : discord.Message):
    """
    Differents commands execution
    """
    cmdmsg = message.content.lower()
    if cmdmsg.startswith("!"):
        iscmdfound = False
        msg_content = str()
        msg_file = None
        if messagesLUT.get(cmdmsg) is not None:
            iscmdfound = True
            msg_content = messagesLUT.get(cmdmsg)
        if filedico.get(cmdmsg) is not None:
            iscmdfound = True
            msg_file = discord.File(filedico.get(cmdmsg))
        if iscmdfound:
            await message.channel.send(content=msg_content, file=msg_file)
    if cmdmsg == "!stop" and message.author.guild_permissions.administrator:
        await bot.close()
    if cmdmsg.startswith("!play"):
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(cmdmsg[6:]))
    if cmdmsg == "!question":
        with open('question.txt', 'r+') as f1:
            question = f1.readline().strip()
            lines = f1.readlines()
            f1.seek(0)
            f1.writelines(lines[0:])
            f1.truncate()
            f1.close()
            await message.channel.send(question)
    if cmdmsg.startswith("!create") and len(cmdmsg) != 7:
        if cmdmsg[8] == "!" and 10+len(command(cmdmsg)) != len(cmdmsg):
            if answer(cmdmsg)[0] != "!":
                messagesLUT[command(cmdmsg)] = answer(cmdmsg)
                await message.channel.send("Command created")
bot.run(key)
