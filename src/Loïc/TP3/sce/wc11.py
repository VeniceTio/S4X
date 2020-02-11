#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# usage: wc11.py file
# variante de wc1.py : ici on utilise l'instruction with
#________________________________________________________
# Affichage du nombre de lignes d'un fichier en paramètre 
#________________________________________________________

import sys

if len(sys.argv[1:]) == 0 :
    sys.stderr.write("argument fichier manquant !\n")
    # idem : print("argument fichier manquant !", file=sys.stderr)
    exit(1)
file = sys.argv[1]

nbl = 0
try:
    with open(file, 'r') as f:	# f est un objet de type file
        while f.readline():
            nbl += 1
    # rem. : close inutile ; fait automatiquement quand on "sort" 
    #        de la portée du <with>

    print("nbre de lignes de", file, ":", nbl)

except: sys.stderr.write("Pb avec " + file + '\n')

