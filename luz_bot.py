# -*- coding: utf-8 -*-

"""
privates tokens
"""
from tkn import key

"""
Lib for the bot
"""
import discord
from fonction import *
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
import requests
from elevenlabs import set_api_key
set_api_key("API-elevenlabs")

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/TxGEqnHWrfWFTfGW9XjX"

default_intents = discord.Intents.default()
default_intents.members = True

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

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
    "!command_2" : 'FILE_2'
}

@bot.event
async def on_message(message : discord.Message):
    """
    Differents commands execution
    """
    cmdmsg = message.content
    if cmdmsg.startswith("!"):
        iscmdfound = False
        msg_content = str()
        msg_file = None
        if command_exist(cmdmsg):
            iscmdfound = True
            msg_content = answ(cmdmsg)
            if filedico.get(cmdmsg) is not None:
                iscmdfound = True
                msg_file = discord.File(filedico.get(cmdmsg))
        if iscmdfound:
            use_command(cmdmsg)
            await message.channel.send(content=msg_content, file=msg_file)
        
        if cmdmsg.startswith("!play"):
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game(cmdmsg[6:]))
        
        if cmdmsg == "!command":
            await message.channel.send(class_commande())
        
        if cmdmsg == "!serveur":
            await message.channel.send(list_serv())

        if cmdmsg == "!user":
            await message.channel.send(class_user())
        
        if cmdmsg == "!stop" and str(message.author) == "ADMIN'S USERNAME":
            await bot.close()

        if (cmdmsg.startswith("!del") and str(message.author) == "ADMIN'S USERNAME" and command_exist(cmdmsg[5:])):
                delcmd(cmdmsg[5:])
                await message.channel.send("Command deleted")
        
        if cmdmsg.startswith("!cd "):
            msg = cmdmsg[4:]
            if serv_exist(msg):
                await message.channel.send(class_commande_serv(msg))
        
        if cmdmsg.startswith("!create") and len(cmdmsg) != 7:
            command_msg = commande(cmdmsg)
            ans_voctxt = reponse(cmdmsg)
            ansmsg = ans_voctxt[0]
            ansvoc = ans_voctxt[1]
            author = message.author
            if cmdmsg[8] == "!" and 10+len(command_msg) != len(cmdmsg):
                if ansmsg[0] != "!" and not(command_exist(command_msg)):
                    if message.guild:
                        serveur = message.guild.name
                        if not(serv_exist(serveur)):
                            add_serv(serveur)
                    else:
                        serveur = "No server"
                    if not(user_exist(author)):
                        add_user(author)
                    add_command(command_msg,ansmsg,author,serveur,ansvoc)
                    await message.channel.send("Command created")
        
        
        if cmdmsg.startswith("!creano") and len(cmdmsg) != 7:
            command_msg = commande(cmdmsg)
            ans_voctxt = reponse(cmdmsg)
            ansmsg = ans_voctxt[0]
            ansvoc = ans_voctxt[1]
            author = "Luzbot"
            if cmdmsg[8] == "!" and 10+len(command_msg) != len(cmdmsg):
                if ansmsg[0] != "!" and not(command_exist(command_msg)):
                    if message.guild:
                        serveur = message.guild.name
                        if not(serv_exist(serveur)):
                            add_serv(serveur)
                    else:
                        serveur = "No server"
                    if not(user_exist(author)):
                        add_user(author)
                    add_command(command_msg,ansmsg,author,serveur,ansvoc)
                    await message.channel.send("Command created")
        
        if cmdmsg.startswith("!voc"):
            msg_content = str()
            msg = cmdmsg[5:]
            if command_exist(msg) and message.author.voice and "http" not in cmdmsg and len(cmdmsg)<500:
                if vocal_exist(msg):
                    msg_content = vocal_cmd(msg)[0]
                else:
                    msg_content = answ(msg)
                channel = message.author.voice.channel
                use_command(msg)
                headers = {
                  "Accept": "audio/mpeg",
                  "Content-Type": "application/json",
                  "xi-api-key": "API-elevenlabs"
                }
                data = {
                  "text": msg_content,
                  "labels": '{"accent": "Français"}',
                  "model_id": "eleven_multilingual_v1",
                  "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.5
                  }
                }
                response = requests.post(url, json=data, headers=headers)
                with open('output.mp3', 'wb') as f:
                    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                        if chunk:
                            f.write(chunk)
                voice_client = await channel.connect()
                audio_source = audio_source = FFmpegPCMAudio('output.mp3', executable='ffmpeg-6.0-full_build\\bin\\ffmpeg.exe')
                voice_client.play(audio_source)
                while voice_client.is_playing():
                    await asyncio.sleep(1)
                await voice_client.disconnect()
        
        if cmdmsg.startswith("!voice"):
            msg = cmdmsg[7:]
            channel = message.author.voice.channel
            if message.author.voice and "http" not in cmdmsg and len(cmdmsg)<500:
                headers = {
                  "Accept": "audio/mpeg",
                  "Content-Type": "application/json",
                  "xi-api-key": "API-elevenlabs"
                }
                data = {
                  "text": msg,
                  "labels": '{"accent": "Français"}',
                  "model_id": "eleven_multilingual_v1",
                  "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.5
                  }
                }
                response = requests.post(url, json=data, headers=headers)
                with open('output.mp3', 'wb') as f:
                    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                        if chunk:
                            f.write(chunk)
                voice_client = await channel.connect()
                audio_source = audio_source = FFmpegPCMAudio('output.mp3', executable='ffmpeg-6.0-full_build\\bin\\ffmpeg.exe')
                voice_client.play(audio_source)
                while voice_client.is_playing():
                    await asyncio.sleep(1)
                await voice_client.disconnect()

        if cmdmsg == "!profil" and user_exist(message.author): 
            msg_profil = {
                "content": None,
                "embeds": [
                {
                    "title": f"It's rewind time for {message.author} !",
                    "color": 5318026,
                    "fields": [
                        {
                            "name": "Commands created",
                            "value": f"{command_created(message.author)}",
                            "inline": True
                        },
                        {
                            "name": "Number of uses",
                            "value": f"{nbr_utilisation_user(message.author)}",
                            "inline": True
                        },
                        {
                            "name": "Most popular order",
                            "value": f"{cmd_fame(message.author)}",
                            "inline": False
                        }
                    ]
                }
            ],
            "username": "Luz",
            "avatar_url": "https://cdn.discordapp.com/attachments/1100456538012926053/1104762606935359569/ce6332144666677.Y3JvcCwyODgwLDIyNTIsMCwyNjU5.png",
            "attachments": []
            }
            embed = discord.Embed.from_dict(msg_profil['embeds'][0])
            await message.channel.send(embed=embed)
        
        
        if cmdmsg.startswith("!profile") and user_exist(cmdmsg[9:]):
            profil = cmdmsg[9:]
            msg_profil = {
                "content": None,
                "embeds": [
                {
                    "title": f"It's rewind time for {profil} !",
                    "color": 5318026,
                    "fields": [
                        {
                            "name": "Commands created",
                            "value": f"{command_created(profil)}",
                            "inline": True
                        },
                        {
                            "name": "Number of uses",
                            "value": f"{nbr_utilisation_user(profil)}",
                            "inline": True
                        },
                        {
                            "name": "Most popular order",
                            "value": f"{cmd_fame(profil)}",
                            "inline": False
                        }  
                    ]
                }
            ],
            "username": "Luz",
            "avatar_url": "https://cdn.discordapp.com/attachments/1100456538012926053/1104762606935359569/ce6332144666677.Y3JvcCwyODgwLDIyNTIsMCwyNjU5.png",
            "attachments": []
            }
            embed = discord.Embed.from_dict(msg_profil['embeds'][0])
            await message.channel.send(embed=embed)
        
        
        if cmdmsg.startswith("!info ") and command_exist(cmdmsg[6:]):
            inf_cmd = cmdmsg[6:]
            msg_profil = {
                "content": None,
                "embeds": [
                {
                    "title": f"It's rewind time for {inf_cmd} !",
                    "color": 5318026,
                    "fields": [
                        {
                            "name": "Creator",
                            "value": f"{creator_cmd(inf_cmd)}",
                            "inline": True
                        },
                        {
                            "name": "Number of uses",
                            "value": f"{nbr_utilisation_cmd(inf_cmd)}",
                            "inline": True
                        },
                        {
                            "name": "Serveur",
                            "value": f"{cmd_serv(inf_cmd)}",
                            "inline": True
                        }
                    ]
                }
            ],
            "username": "Luz",
            "avatar_url": "https://cdn.discordapp.com/attachments/1100456538012926053/1104762606935359569/ce6332144666677.Y3JvcCwyODgwLDIyNTIsMCwyNjU5.png",
            "attachments": []
            }
            embed = discord.Embed.from_dict(msg_profil['embeds'][0])
            await message.channel.send(embed=embed)

bot.run(key)
