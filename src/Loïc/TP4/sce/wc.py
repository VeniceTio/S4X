#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# usage: wc.py file
#________________________________________________________
# Affichage du nombre de lignes d'un fichier en paramètre 
# On utilise la fonction OPEN
#_______________________________________________________

import os, sys

if len(sys.argv[1:]) == 0 :
    sys.stderr.write("argument fichier manquant !\n")
    exit(1)
file = sys.argv[1]
if not os.path.isfile(file) :
    msg = file + " n'est pas un fichier regulier\n"
    sys.stderr.write(msg)
    exit(1)

nbl = 0
f = open(file, 'r') 	# f est un objet de type file

# parcours ligne apres ligne
while f.readline() :
	nbl += 1	# nbl = nbl + 1

f.close()
print("nbre de lignes de", file, ":", nbl)

print("avec deuxieme methode")
# variante => notation "ensembliste"
# ______________________
f = open(file) 	
nbl = 0
for ligne in f : nbl += 1
# affichage possible de la ligne lue par: print ligne
# ______________________

f.close()
print("nbre de lignes de", file, ":", nbl)
