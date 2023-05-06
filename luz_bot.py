# -*- coding: utf-8 -*-

"""
privates tokens
"""
from tkn import key # key : discord bot token // Other : Channels ID

"""
Lib for the bot
"""
import discord
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
async def on_disconnect():
    """
    Tell the dev when the bot is offline
    """
    print("The bot is offline")

filedico = {
    "!command" : 'FILE',
    "!command_2" : 'FILE_2',
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
        if cmdmsg.startswith("!play"):
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game(cmdmsg[6:]))
        if cmdmsg == "!commands":
            await message.channel.send(str(messagesLUT.keys())[9:].strip("()[]").replace(",", "\n"))
        if cmdmsg.startswith("!create") and len(cmdmsg) != 7:
            commande_msg = command(cmdmsg)
            answer_msg = answer(cmdmsg)
            if cmdmsg[8] == "!" and 10+len(commande_msg) != len(cmdmsg):
                if answer_msg[0] != "!":
                    messagesLUT[commande_msg] = answer_msg
                    save(f"{commande_msg}"+" : "+f"{answer_msg}"+" ,")
                    await message.channel.send("Command created")
bot.run(key)
