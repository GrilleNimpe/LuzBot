# -*- coding: utf-8 -*-

"""
privates tokens
"""
from tkn import key

"""
Lib for the bot
"""
import discord
from fonction_sqlite import *
from commande import *
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
import requests
from elevenlabs import set_api_key
set_api_key("CLE DE L'API")

CHUNK_SIZE = 1024
url = "URL VERS L'API"

default_intents = discord.Intents.default()
default_intents.members = True

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

# Affiche "Le bot est connecté" lorsque celui ci est prêt à être utiliser.
@bot.event
async def on_ready():
    print("Le bot est connecté")

# Affiche "Le bot est déconnecté" lorsque celui ci est déconnecté
@bot.event
async def on_disconnect():
    print("Le bot est déconnecté")

@bot.event
async def on_message(message : discord.Message):
    """
    Differents commands execution
    """
    cmdmsg = message.content

    # Utilisation d'une commande créée.
    if cmdmsg[0] == "!":
        iscmdfound = False
        msg_content = str()
        msg_file = None
        if command_exist(cmdmsg):
            iscmdfound = True
            msg_content = recup_commande(cmdmsg)
            if filedico.get(cmdmsg) is not None:
                iscmdfound = True
                msg_file = discord.File(filedico.get(cmdmsg))
        if iscmdfound:
            utilisation_commande(cmdmsg)
            await message.channel.send(content=msg_content, file=msg_file)
        
        # Force Luz à jouer.
        if cmdmsg.startswith("!play "):
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game(cmdmsg[6:]))
        
        # Classement des meilleurs commandes
        if cmdmsg == "!commande":
            await message.channel.send(class_commande())
        
        #Liste les serveurs
        if cmdmsg == "!serveur":
            await message.channel.send(list_serv())

        # Classement des meilleurs utilisateurs
        if cmdmsg == "!user":
            await message.channel.send(class_user())
        
        # Arrête le bot.
        if cmdmsg == "!stop" and str(message.author) == "NOM DE L'ADMIN":
            await bot.close()

        #Supprime une commande
        if (cmdmsg.startswith("!del !") and str(message.author) == "NOM DE L'ADMIN" and command_exist(cmdmsg[5:])):
                supprimer(cmdmsg[5:])
                await message.channel.send("Commande supprimée")

        # Consulter les commandes d'un serveur
        if cmdmsg.startswith("!cd "):
            msg = cmdmsg[4:]
            if serv_exist(msg):
                await message.channel.send(class_commande_serv(msg))
        
        #Création d'une nouvelle commande
        if cmdmsg.startswith("!create !"):
            infos_commande = commande(cmdmsg)# On récupère l'apppel, la réponse textuel et la réponse vocal de la commande
            auteur = message.author
            if infos_commande.rep[0] != "!" and not(command_exist(infos_commande.appel)): #Vérifie que la reponse n'appelle pas une autre commande et que la commande n'existe pas.
                if message.guild:# La commande est créé depuis un serveur
                    serveur = message.guild.name
                    if not(serv_exist(serveur)):# Luz ne reconnait pas le serveur
                        add_serv(serveur)# On ajoute le nom du serveur à Luz
                else:
                    serveur = "No server"
                if not(user_exist(auteur)):# Luz ne reconnait pas l'utilisateur
                    add_user(auteur)# On ajoute le nom de l'utilisateur à Luz
                add_commande(infos_commande.appel,infos_commande.rep,auteur,serveur,infos_commande.voc)# On ajoute la commande à Luz.
                await message.channel.send("Commande créée")
        
        #Création d'une nouvelle commande mais annonyment
        if cmdmsg.startswith("!creano !") and len(cmdmsg) != 7:
            infos_commande = commande(cmdmsg)# On récupère l'apppel, la réponse textuel et la réponse vocal de la commande
            auteur = "Luzbot"
            if infos_commande.rep[0] != "!" and not(command_exist(infos_commande.appel)): #Vérifie que la reponse n'appelle pas une autre commande et que la commande n'existe pas.
                if message.guild:# La commande est créé depuis un serveur
                    serveur = message.guild.name
                    if not(serv_exist(serveur)):# Luz ne reconnait pas le serveur
                        add_serv(serveur)# On ajoute le nom du serveur à Luz
                else:
                    serveur = "No server"
                add_commande(infos_commande.appel,infos_commande.rep,auteur,serveur,infos_commande.voc)# On ajoute la commande à Luz.
                await message.channel.send("Commande créée")
        
        #Utilisation d'une commande vocal
        if cmdmsg.startswith("!voc !"):
            msg_content = str()
            msg = cmdmsg[5:]# On récupère le nom de la commande
            if command_exist(msg) and message.author.voice and len(cmdmsg)<500:
                if vocal_exist(msg):# Est ce que une réponse vocal existe pour cette commande ?
                    msg_content = vocal_cmd(msg)[0]# Oui, on l'a récupère
                else:
                    msg_content = recup_commande(msg)#Non on récupère la commande textuel
                if "http" not in msg_content:
                    channel = message.author.voice.channel
                    utilisation_commande(msg)
                    headers = {
                        "Accept": "audio/mpeg",
                        "Content-Type": "application/json",
                        "xi-api-key": "CLE DE L'API"
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
        
        # Utilisation de la voix de Luz (sans créer de commandes)
        if cmdmsg.startswith("!voice "):
            msg = cmdmsg[7:]# On récupère ce qui va être dit.
            channel = message.author.voice.channel
            if message.author.voice and "http" not in cmdmsg and len(cmdmsg)<500:
                headers = {
                  "Accept": "audio/mpeg",
                  "Content-Type": "application/json",
                  "xi-api-key": "CLE DE L'API"
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
                audio_source = audio_source = FFmpegPCMAudio('output.mp3', executable='CHEMIN VERS "ffmpeg.exe"')
                voice_client.play(audio_source)
                while voice_client.is_playing():
                    await asyncio.sleep(1)
                await voice_client.disconnect()

        # Renvoie le profile de l'utilisateur.
        if cmdmsg == "!profile" and user_exist(message.author) and len(cmdmsg) != 8: 
            msg_profile = {
                "content": None,
                "embeds": [
                {
                    "title": f"C'est l'heure du rewind de {message.author} !",
                    "color": 5318026,
                    "fields": [
                        {
                            "name": "Commandes créée",
                            "value": f"{commande_créée(message.author)}",
                            "inline": True
                        },
                        {
                            "name": "Nombre d'utilisations",
                            "value": f"{nbr_utilisation_user(message.author)}",
                            "inline": True
                        },
                        {
                            "name": "Commande la plus populaire",
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
            embed = discord.Embed.from_dict(msg_profile['embeds'][0])
            await message.channel.send(embed=embed)
        
        # Renvoie le profile d'un utilisateur.
        if cmdmsg.startswith("!profile") and user_exist(cmdmsg[9:]):
            profile = cmdmsg[9:]
            msg_profile = {
                "content": None,
                "embeds": [
                {
                    "title": f"C'est l'heure du rewind de {profile} !",
                    "color": 5318026,
                    "fields": [
                        {
                            "name": "Commandes créée",
                            "value": f"{commande_créée(profile)}",
                            "inline": True
                        },
                        {
                            "name": "Nombre d'utilisations",
                            "value": f"{nbr_utilisation_user(profile)}",
                            "inline": True
                        },
                        {
                            "name": "Commande la plus populaire",
                            "value": f"{cmd_fame(profile)}",
                            "inline": False
                        }  
                    ]
                }
            ],
            "username": "Luz",
            "avatar_url": "https://cdn.discordapp.com/attachments/1100456538012926053/1104762606935359569/ce6332144666677.Y3JvcCwyODgwLDIyNTIsMCwyNjU5.png",
            "attachments": []
            }
            embed = discord.Embed.from_dict(msg_profile['embeds'][0])
            await message.channel.send(embed=embed)
        
        # Renvoie les infos d'une commande.
        if cmdmsg.startswith("!info !") and command_exist(cmdmsg[6:]):
            inf_cmd = cmdmsg[6:]
            msg_profile = {
                "content": None,
                "embeds": [
                {
                    "title": f"C'est l'heure du rewind de {inf_cmd} !",
                    "color": 5318026,
                    "fields": [
                        {
                            "name": "Créateur",
                            "value": f"{createur_cmd(inf_cmd)}",
                            "inline": True
                        },
                        {
                            "name": "Nombre d'utilisations",
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
            embed = discord.Embed.from_dict(msg_profile['embeds'][0])
            await message.channel.send(embed=embed)

bot.run(key) #Saisir la clé du bot
