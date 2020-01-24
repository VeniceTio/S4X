#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# usage: wc1.py file
#________________________________________________________
# Affichage du nombre de lignes d'un fichier en paramètre 
#________________________________________________________
# On utilise la fonction open
# avec une gestion d'EXCEPTION
#________________________________________________________

import sys

if len(sys.argv[1:]) == 0 :
    sys.stderr.write("argument fichier manquant !\n")
    # idem : print("argument fichier manquant !", file=sys.stderr)
    exit(1)
file = sys.argv[1]

nbl = 0
try: 
    f = open(file, 'r') 	# f est un objet de type file
except IOError: 
    sys.stderr.write("Pb ouverture de " + file + '\n')
    # print("Pb ouverture de", file, file=sys.stderr)
else:  				# si ouverture ok
# parcours du fichier ligne apres ligne
    while f.readline() :
        nbl += 1	# nbl = nbl + 1

    f.close()
    print("nbre de lignes de", file, ":", nbl)

