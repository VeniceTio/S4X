#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# nba_nation_parent.py

import sys,subprocess,datetime
from os.path import basename


def traiteListe(nation):
    pipe = subprocess.Popen(["./nba_nation_subproc.py", nation], stdout=subprocess.PIPE, universal_newlines=True)
    annee_courante = datetime.date.today().year

    nbf = 0
    ligne = pipe.stdout.readline()
    while ligne:           # on lit dans le "pipe" associé à la commande "ls -a"
        ligne = ligne[:-1] # on se debarrasse du \n de fin de ligne
        ligne = ligne[:-1]  # on se débarrasse du '\n' de fin de ligne
        if ligne.endswith(nation):
            nom, _, club, annee_nais, _ = ligne.split(':')  # conversion de la chaine en tableau
            age = annee_courante - int(annee_nais)
            print(nom + ', ' + club + ', ' + str(age))
        ligne = pipe.stdout.readline()

if __name__ == "__main__" :
    nom_fichier='nba_2019.txt'
    if len(sys.argv[1:]) == 1 :
        nation = sys.argv[1]
    else :
        sys.stderr.write("Usage : " + basename(sys.argv[0]) + " nation\n")
        exit(1)

    try:
        joueurs = open(nom_fichier, 'r')
    except IOError:
        msg = nom_fichier + ": Pb ouverture !\n"
        sys.stderr.write(msg)
    else:
        traiteListe(nation)


