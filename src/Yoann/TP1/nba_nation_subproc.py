#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# nba_nation_subproc.py

'''
Structure du fichier nba_2019.txt dont on suppose qu'il est ds le repertoire courant :
prenom nom:taille:club:annee_naissance:nation
Exemples valeur de nation : us, fr, es, gr

Liste les basketteurs de la nba dont la nationalité est la nation passée en paramètre
On affiche juste les infos "prenom nom, club et age"
'''

from os.path import basename, isfile
from sys import stderr, argv

def traiter_fichier(joueurs):
    chaine = []
    for un_joueur in joueurs:
        un_joueur = un_joueur[:-1]
        if un_joueur.endswith(nation):
            chaine += [un_joueur]
    joueurs.close()
    return chaine


nom_fichier='nba_2019.txt'
if len(argv[1:]) == 1 :
    nation = argv[1]
else :
    stderr.write("Usage : " + basename(argv[0]) + " nation\n")
    exit(1)

try:
    joueurs = open(nom_fichier, 'r')
except IOError:
    msg = nom_fichier + ": Pb ouverture !\n"
    stderr.write(msg)
else:
    tab = traiter_fichier(joueurs)
    joueurs.close()
    for i in range(0, len(tab)):
        print(tab[i])