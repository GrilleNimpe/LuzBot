# -*- coding: utf-8 -*-

"""
Lib for the bot
"""
import discord

default_intents = discord.Intents.default()
default_intents.value = 32511 # escape a pylint false error, same as default_intents.members = True
print(default_intents.members)

tkn = input("Enter token: ")
welcome_channel = input("Enter welcome channel token: ")
goodbye_channel = input("Enter goodbye channel token: ")
update_channel = input("Enter update channel token: ")

client = discord.Client(intents=default_intents)


@client.event
async def on_ready():
    """
    Tell the dev when the bot is online
    """
    print("Le bot est connecté")

@client.event
async def on_member_join(member):
    """
    Greetings when a member join a guild
    """
    bienvenue: discord.TextChannel = client.get_channel(welcome_channel)
    await bienvenue.send(content=
        f"Un giga beau gosse vient d'arriver sur le serveur, son nom est {member.display_name} !"
    )

@client.event
async def on_member_remove(member):
    """
    Goodbye when a member leave a guild
    """
    a_la_prochaine: discord.TextChannel = client.get_channel(goodbye_channel)
    await a_la_prochaine.send(content=f"A la revoyure {member.display_name} !")

@client.event
async def on_disconnect():
    """
    Tell the dev when the bot is offline
    """
    print("Le bot est déconnecté")

@client.event
async def on_member_update(before, after):
    """
    Inform the guild when a member change his name
    """
    changement: discord.TextChannel = client.get_channel(update_channel)
    if {before.display_name} == {after.display_name}:
        print("changement inutile")
    else:
        await changement.send(content=f"{before.display_name} est devenue {after.display_name} !")

messagesLUT = {
    "!lpsdd" :
        "https://discord.gg/HyQ9mPd5",
    "!farkdateproduction" :
        "https://www.youtube.com/channel/UC0f0m2dVJSu9TXkh23Unhhw/featured",
    "!6" :
        "Saucisse",
    "!7" :
        "Chaussette",
    "!toto" :
        "Patate au BEUR",
    "!beur" :
        "Brassière est un robot BIP BOUP",
    "!koopafdp" :
        "🍆",
    "!bonluz" :
        "*vous carressez Luz*",
    "!help" :
        """
> Luz souhaite la bienvenue lorsque qu'un nouveau membre se joint à La Tavola
> Luz dit adieux à ceux qui nous quitte (triste)
> Luz prévient lorsque des membres changent de pseudo afin de les reconnaître
`!toto` pour avoir son nom de code
`!farkdateproduction` pour avoir accès à une chaîne youtube tenue par des chads
`!lpsdd` pour rejoindre l'élite de la société
`!inf/surv/plombier` pour BEUR
`!6` saucisse
`!7` chaussette
`!beur` rasberry BIP BOUP
`!koopafdp` : chef de l'élite de la société
`!bonluz` pour luz :)
        """,
    "!code" :
        """
Salle à manger : Perm
Cuisine : CDI
Patate : session
Patate au plomb : plombier
Viande : Veyon
Cuire une patate : Shutdown un pc
Patate au BEUR : toto
Lipo : technicien
BEUR : Bansière est un robot
IEUC : Ivan est un cyborg
EEUC : Ethan est un capteur
        """
}

fileLUT = {
    "!bonluz" :
        'unknown.gif'
}

@client.event
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
        if fileLUT.get(cmdmsg) is not None:
            iscmdfound = True
            msg_file = discord.File(fileLUT.get(cmdmsg))
        if iscmdfound:
            await message.channel.send(content=msg_content, file=msg_file)
    if cmdmsg == "!stop" and message.author.guild_permissions.administrator:
        await client.close()

client.run(tkn) #Saisir la clé du bot
