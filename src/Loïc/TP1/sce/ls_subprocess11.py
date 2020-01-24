#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# ls_subprocess11.py
''' Affichage des noms des fichiers reguliers (caches ou non)
              et du nombre de fichiers du repertoire courant
'''
# Principe: communication par "pipe" entre la commande 'ls' et le script python

import os
import subprocess

# lancement d'une commande unix qui s'execute dans un sous-processus
# l'argument stdout est utile pour que le script python puisse lire les
# resultats (la sortie standard) de ce sous-processus
pipe = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE, universal_newlines=True)
# pipe = subprocess.Popen('ls -a', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

# différence par rapport à <ls_process1.py> :
# emploi du paramètre universal_newlines=True dans le constructeur Popen pour ne pas 
# avoir besoin d'utiliser la fonction decode() qui fait la conversion byte string => str 

nbf = 0
ligne = pipe.stdout.readline()
while ligne:           # on lit dans le "pipe" associé à la commande "ls -a"
    ligne = ligne[:-1] # on se debarrasse du \n de fin de ligne
    if os.path.isfile(ligne):
        print(ligne)
        nbf += 1  # nbf = nbf + 1
    ligne = pipe.stdout.readline()

pipe.stdout.close()
print("Nombre de fichiers ordinaires: ", nbf)
exit()

# variante style "ensembliste" pour le parcours des lignes de resultat
for ligne in pipe.stdout:
    ligne = ligne[:-1] # on se debarrasse du \n de fin de ligne
    if os.path.isfile(ligne):
        print(ligne)
        nbf += 1
