class Commande:
    def __init__(self, appel, reponse, vocal):
        self.appel = appel
        self.rep = reponse
        self.voc = vocal

def commande(msg):
    # On va prendre pour exemple msg = "!create !test : test textuel réussi !voc test vocal réussi"
    appel_com = msg[8] # On récupère le "!" de !test
    i = 9
    while msg[i+1] != ":":
        #On récupère le reste de l'appel de la commande, ici !test
        appel_com += msg[i]
        i += 1   
    
    reponse_com = msg[i+3]# On récupère le premier caractère de la réponse, ici "t"
    i += 4
    longueur_limite = len(msg)-11
    while msg[i+1:i+5] != "!voc" and len(appel_com) != longueur_limite - len(reponse_com):
        #On récupère la réponse textuel de la commande
        reponse_com += msg[i]
        i += 1   

    if longueur_limite - len(reponse_com) != len(appel_com):#Si il y a !voc dans le message
        i += 6
        vocal_com = msg[i:]
    else:
        vocal_com = None
    
    return(Commande(appel_com,reponse_com,vocal_com))

# Liste des fichiers audio pour Luz
filedico = {
    "!commande1" : 'fichier1',
    "!commande2" : 'fichier2'
}

"""
cmd = "!create !test : test textuel réussi !voc test vocal réussi"
res = commande(cmd)
print(res.appel)
print(res.rep)
print(res.voc)
"""
