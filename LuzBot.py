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

messagesLUT = {
    "!lpsdd" : "https://discord.gg/HyQ9mPd5",
    "!farkdateproduction" : "https://www.youtube.com/channel/UC0f0m2dVJSu9TXkh23Unhhw/featured",
    "!6" : "Saucisse",
    "!7" : "Chaussette",
    "!toto" : "Patate au BEUR",
    "!beur" : "Brassière est un robot BIP BOUP",
    "!koopafdp" : "🍆",
    "!bonluz" : "!help",
    "!help" :   "> Luz peut souhaiter la bienvenue lorsque qu'un nouveaux membre se joint à La Tavola"+"\n"+
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
                "`!bonluz` pour luz :)",
    "!code" :   "Salle à manger : Perm"+"\n"+
                "Cuisine : CDI"+"\n"+
                "Patate : session"+"\n"+
                "Patate au plomb : plombier"+"\n"+
                "Viande : Veyon"+"\n"+
                "Cuire une patate : Shutdown un pc"+
                "\n"+"Patate au BEUR : toto"+"\n"+
                "Lipo : technicien"+"\n"+
                "BEUR : Banssière est un robot"+"\n"+
                "IEUC : Ivan est un cyborg"+"\n"+
                "EEUC : Ethan est un capteur"
}

@client.event
async def on_message(message):
    cmdmsg = message.content.lower()
    if (cmdmsg.startswith("!") and messagesLUT.get(cmdmsg) != None):
        await message.channel.send(messagesLUT.get(cmdmsg))

client.run() #Saisir la clé du bot