#!/usr/bin/python3
# -*- coding: utf8 -*-
# nba_par_nation.py  nation

'''
Structure du fichier nba_2019.txt dont on suppose qu'il est ds le repertoire courant :
prenom nom:taille:club:annee_naissance:nation
Exemples valeur de nation : us, fr, es, gr (greece)

Liste les basketteurs de la nba dont la nationalité est la nation passée en paramètre
On affiche juste les infos "prenom nom, club et age"
'''

import sys, os
import datetime

if len(sys.argv[1:]) == 1 :
    nation = sys.argv[1]
else :
    sys.stderr.write("Usage : " + os.path.basename(sys.argv[0]) + " nation\n")
    exit(1)

if not os.path.isfile('nba_2019.txt') :
    msg = 'nba_2019.txt' + ": fichier inexistant !\n"
    sys.stderr.write(msg)
    exit(1)

joueurs = open('nba_2019.txt', 'r')
annee_courante = datetime.datetime.now().year

un_joueur = joueurs.readline()[:-1] # on se debarrasse du '\n' de fin de ligne
while un_joueur:
    if un_joueur.endswith(nation):
        nom, _ , club, annee_nais, _ = un_joueur.split(':')  # conversion de la chaine en tableau
        age = annee_courante - int(annee_nais)
        print(nom + ', ' + club + ', ' + str(age))
    un_joueur = joueurs.readline()[:-1]

joueurs.close()

# Affichage avec alignement des colonnes à gauche
print('\nAffichage avec alignement des colonnes à gauche')
input('Appuyer sur Entree')
print()

# Reouverture du fichier
joueurs = open('nba_2019.txt', 'r')

un_joueur = joueurs.readline()[:-1] # on se debarrasse du '\n' de fin de ligne
while un_joueur:
    if un_joueur.endswith(nation):
        nom, _ , club, annee_nais, _ = un_joueur.split(':')  # conversion de la chaine en tableau
        age = annee_courante - int(annee_nais)
        print( '{0:18s}| {1:26s}| {2:d} ans'.format(nom, club, age) )
        # print( '%-18s| %-26s| %2d ans' %(nom, club, age) )
    un_joueur = joueurs.readline()[:-1]

joueurs.close()

