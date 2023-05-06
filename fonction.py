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

def question():
    with open('question.txt', 'r+') as f1:
            qst = f1.readline().strip()
            lines = f1.readlines()
            f1.seek(0)
            f1.writelines(lines[0:])
            f1.truncate()
            f1.close()
    return(qst)

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
> Luz can ask a question to start a conversation
> Luz doesn't look like that but he's a real chad, he just can't clean.
> Luz can play any game you want (even those that don't exist)
        """,
    "!command":
        "ANSWER",
    "!command_2":
        "ANSWER_2"
}
