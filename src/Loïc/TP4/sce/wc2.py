#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# usage: wc2.py file
#________________________________________________________
# Affichage du nombre de lignes d'un fichier en paramètre 
#________________________________________________________
#
# utilisation de la fonction readlines() qui lit "en un coup" 
#                            le fichier complet
#_______________________________________________________

from sys import stderr, argv
from os.path import isfile

if len(argv[1:]) == 0 :
    stderr.write("argument fichier manquant !\n")
    exit(1)

file = argv[1]
if not isfile(file) :
    msg = file + " n'est pas un fichier regulier\n"
    stderr.write(msg)
    exit(1)

f = open(file, 'r') 	# f est un objet de type file

print("nbre de lignes de", file, ":", len(f.readlines()))
# rem: avec readlines() on recupere le fichier complet en memoire
# inconvenient: peut "planter" si fichier trop volumineux

f.close()
