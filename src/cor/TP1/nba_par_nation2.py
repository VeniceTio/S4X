#!/usr/bin/python3
# -*- coding: utf8 -*-
# nba_par_nation2.py  nation
# variante de nba_par_nation.py

'''
Structure du fichier nba_2019.txt dont on suppose qu'il est ds le repertoire courant :
prenom nom:taille:club:annee_naissance:nation
Exemples valeur de nation : us, fr, es, gr

Liste les basketteurs de la nba dont la nationalité est la nation passée en paramètre
On affiche juste les infos "prenom nom, club et age"
'''

from os.path import basename, isfile
from sys import stdout, stderr, argv
from datetime import datetime

def traiter_fichier(joueurs):
    annee_courante = datetime.now().year
    for un_joueur in joueurs:
        un_joueur = un_joueur[:-1] # on se débarrasse du '\n' de fin de ligne
        if un_joueur.endswith(nation):
            nom, _ , club, annee_nais, _ = un_joueur.split(':')  # conversion de la chaine en tableau
            age = annee_courante - int(annee_nais)
            print(nom + ', ' + club + ', ' + str(age))
    joueurs.close()

    # Affichage avec alignement des colonnes à gauche
    print('\nAffichage avec alignement des colonnes à gauche')
    input('Appuyer sur Entree')
    print()

    # Reouverture du fichier
    # global nom_fichier
    joueurs = open(nom_fichier, 'r')

    for un_joueur in joueurs:
        un_joueur = un_joueur[:-1] # on se débarrasse du '\n' de fin de ligne
        if un_joueur.endswith(nation):
            un_joueur = un_joueur.split(':')
            age = annee_courante - int(un_joueur[3])
            print( '{0:18s}| {1:26s}| {2:d} ans'.format(un_joueur[0], un_joueur[2], age) )

if __name__ == "__main__" :
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
        traiter_fichier(joueurs)
        joueurs.close()
