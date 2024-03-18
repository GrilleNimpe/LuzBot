# -*- coding: utf-8 -*-
import sqlite3

"""Fonction SQLite"""


def comand_exist(message):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute(f'SELECT answer FROM Commande WHERE command = ?', (message,))
    resultat = cur.fetchone()
    conn.commit()
    conn.close()
    return(resultat != None)

def serv_exist(message):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute(f'SELECT id_serveur FROM Luztable WHERE serveur = ?', (message,))
    resultat = cur.fetchone()
    conn.commit()
    conn.close()
    return(resultat != None)

def user_exist(message):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('SELECT id_user FROM User WHERE name = ?', (message,))
    resultat = cur.fetchone()
    conn.commit()
    conn.close()
    return(resultat != None)


def recup_commande(message):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('SELECT answer FROM Commande WHERE command = ?', (message,))
    resultat = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return resultat

def utilisation_commande(message):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('UPDATE Commande SET utilisation = utilisation + 1 WHERE command = ?', (message,))
    cur.execute('UPDATE User SET use = use + 1 WHERE id_user = (SELECT id_user FROM Commande WHERE command = ?)', (message,))
    conn.commit()
    conn.close()

def supprimer(message):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('UPDATE User SET creation = creation - 1 WHERE id_user = (SELECT id_user FROM Commande WHERE command = ?)', (message,))
    cur.execute('DELETE FROM Commande WHERE command = ?', (message,))
    conn.commit()
    conn.close()


def add_user(user):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO User (name, use, creation) VALUES (?, 0, 1)', (user,))
    conn.commit()
    conn.close()

def add_commande(cmd, ans, user, serv, voc):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO Commande (command, answer, utilisation, id_user, id_serveur, vocal) VALUES (?, ?, 0, (SELECT id_user FROM User WHERE name = ?), (SELECT id_serveur FROM Luztable WHERE serveur = ?), ?)', (cmd, ans, user, serv, voc))
    cur.execute('UPDATE User SET creation = creation + 1 WHERE id_user = (SELECT id_user FROM Commande WHERE command = ?)', (cmd,))
    conn.commit()
    conn.close()
def commande_creee(user):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('SELECT creation FROM User WHERE name = ?', (user,))
    resultat = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return resultat

def nbr_utilisation_user(user):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('SELECT use FROM User WHERE name = ?', (user,))
    resultat = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return resultat

def createur_cmd(cmd):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('SELECT name FROM User WHERE id_user = (SELECT id_user FROM Commande WHERE command = ?)', (cmd,))
    resultat = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return(resultat)

def nbr_utilisation_cmd(cmd):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute(f'SELECT utilisation FROM Commande WHERE command = ?', (cmd,))
    resultat = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return(resultat)

def cmd_serv(cmd):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute(f'SELECT serveur FROM Luztable WHERE id_serveur = (SELECT id_serveur FROM Commande WHERE command = ?)', (cmd,))
    resultat = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return(resultat)

def class_commande():
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('SELECT command, utilisation FROM Commande ORDER BY utilisation DESC')
    data = cur.fetchall()
    conn.commit()
    conn.close()
    strings_list = [f"{item[0]}, {item[1]} utilisation" for item in data]
    resultat = '\n'.join(strings_list)
    lignes = resultat.split('\n')
    numerotees = [f"{i+1}. {ligne}" for i, ligne in enumerate(lignes)]
    return('\n'.join(numerotees))

def class_user():
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('SELECT name, use FROM User ORDER BY use DESC')
    data = cur.fetchall()
    conn.commit()
    conn.close()
    strings_list = [item[0] for item in data]
    resultat = '\n'.join(strings_list)
    lignes = resultat.split('\n')
    numerotees = [f"{i+1}. {ligne}" for i, ligne in enumerate(lignes)]
    return('\n'.join(numerotees))

def cmd_fame(profile):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute(f'SELECT command FROM Commande WHERE id_user = (SELECT id_user FROM User WHERE name = ?) ORDER BY utilisation DESC', (profile,))
    resultat = cur.fetchone()
    if resultat == None:
        resultat = ["None"]
    conn.commit()
    conn.close()
    return(resultat[0])

def vocal_exist(message):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute(f'SELECT vocal FROM Commande WHERE command = ?', (message,))
    resultat = cur.fetchone()
    conn.commit()
    conn.close()
    return(resultat[0] != None)

def vocal_cmd(message):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute(f'SELECT vocal FROM Commande WHERE command = ?', (message,))
    resultat = cur.fetchone()
    conn.commit()
    conn.close()
    return(resultat)

def list_serv():
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute('SELECT serveur FROM Luztable')
    data = cur.fetchall()
    conn.commit()
    conn.close()
    strings_list = [f"{item[0]}" for item in data]
    resultat = '\n'.join(strings_list)
    lignes = resultat.split('\n')
    numerotees = [f"{i+1}. {ligne}" for i, ligne in enumerate(lignes)]
    return('\n'.join(numerotees))

def class_commande_serv(serv):
    conn = sqlite3.connect('luzdata.db')
    cur = conn.cursor()
    cur.execute(f'SELECT command, utilisation FROM Commande WHERE id_serveur = (SELECT id_serveur FROM Luztable WHERE serveur = ?) ORDER BY utilisation DESC', (serv,))
    data = cur.fetchall()
    conn.commit()
    conn.close()
    strings_list = [f"{item[0]}, {item[1]} utilisation" for item in data]
    resultat = '\n'.join(strings_list)
    lignes = resultat.split('\n')
    numerotees = [f"{i+1}. {ligne}" for i, ligne in enumerate(lignes)]
    return('\n'.join(numerotees))
