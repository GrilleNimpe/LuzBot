# -*- coding: utf-8 -*-
def command(cara):
    com = cara[8:][0]
    i = 9
    while cara[i] != ":" and len(com) < len(cara):
        com += cara[i]
        i += 1
    return(com.rstrip(" "))

def answer(cara):
    return(cara[11+len(command(cara)):])

def save(chaine):
    with open("commands.txt","a",encoding="utf-8") as f:
        f.write(chaine)
        f.close()
messagesLUT = {
    "!farkdateproduction" :
        "https://www.youtube.com/channel/UC0f0m2dVJSu9TXkh23Unhhw",
    "!help" :
        """
`!commands` To list the commands
`!create !command : answer` Please respect the spaces
> Luz has some really cool commands
> Luz doesn't look like that but he's a real chad, he just can't clean.
> Luz can play any game you want (even those that don't exist) with !play
        """,
    "!command":
        "ANSWER",
    "!command_2":
        "ANSWER_2"
}
