# -*- coding: utf-8 -*-
import discord

default_intents = discord.Intents.default()
default_intents.members = True

client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print("Le bot est connecté")

@client.event
async def on_member_join(member):
    bienvenue: discord.TextChannel = client.get_channel() #Saisir la clé du channel
    await bienvenue.send(content=f"Un giga beau gosse vient d'arriver sur le serveur, son nom est {member.display_name} !")

@client.event
async def on_member_remove(member):
    à_la_prochaine: discord.TextChannel = client.get_channel() #Saisir la clé du channel
    await à_la_prochaine.send(content=f"A la revoyure {member.display_name} !")

@client.event
async def on_disconnect():
    print("Le bot est déconnecté")

@client.event
async def on_member_update(before, after):
    changement: discord.TextChannel = client.get_channel() #Saisir la clé du channel
    if {before.display_name} == {after.display_name}:
        print("changement inutile")
    else:
        await changement.send(content=f"{before.display_name} est devenue {after.display_name} !")


@client.event
async def on_message(message):
    if message.content.lower() == "!lpsdd":
        await message.channel.send("https://discord.gg/HyQ9mPd5")
    if message.content.lower() == "!farkdateproduction":
        await message.channel.send("https://www.youtube.com/channel/UC0f0m2dVJSu9TXkh23Unhhw/featured")
    if message.content.lower() == "!6":
        await message.channel.send("Saucisse")
    if message.content.lower() == "!7":
        await message.channel.send("Chaussette")
    if message.content.lower() == "!toto":
        await message.channel.send("Patate au BEUR")
    if message.content.lower() == "!beur":
        await message.channel.send("Brassière est un robot BIP BOUP")
    if message.content.lower() == "!koopafdp":
        await message.channel.send("🍆")
    if message.content.lower() == "!bonluz":
       await message.channel.send(file=discord.File('unknown.gif'))
    if message.content.lower() == "!help":
        await message.channel.send("> Luz peut souhaiter la bienvenue lorsque qu'un nouveaux membre se joint à La Tavola"+"\n"+
                                   "> Luz peut dire adieux à ceux qui nous quitte (triste)"+"\n"+
                                   "> Luz prévient les autres membres lorsqu'ils changent de pseudo afin de ne pas les prêter à confusion"+"\n"+
                                   "`!toto` pour avoir son nom de code"+"\n"+
                                   "`!farkdateproduction` pour avoir accès à une chaîne youtube tenu par des chads"+"\n"+
                                   "`!lpsdd` pour rejoindre l'élite de la société"+
                                   "\n"+"`!inf/surv/plombier` pour BEUR"+"\n"+
                                   "`!6` saucisse"+"\n"+
                                   "`!7` chaussette"+"\n"+
                                   "`!beur` rasberry BIP BOUP"+"\n"+
                                   "`!koopafdp` : chef de l'élite de la société"+"\n"+
                                   "`!bonluz` pour luz :)")
    if message.content.lower() == "!code":
        await message.channel.send("Salle à manger : Perm"+"\n"+
                                   "Cuisine : CDI"+"\n"+
                                   "Patate : session"+"\n"+
                                   "Patate au plomb : plombier"+"\n"+
                                   "Viande : Veyon"+"\n"+
                                   "Cuire une patate : Shutdown un pc"+
                                   "\n"+"Patate au BEUR : toto"+"\n"+
                                   "Lipo : technicien"+"\n"+
                                   "BEUR : Banssière est un robot"+"\n"+
                                   "IEUC : Ivan est un cyborg"+"\n"+
                                   "EEUC : Ethan est un capteur")


    
client.run() #Saisir la clé du bot