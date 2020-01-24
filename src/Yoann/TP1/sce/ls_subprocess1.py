#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# ls_subprocess1.py
''' Affichage des noms des fichiers reguliers (caches ou non)
              et du nombre de fichiers du repertoire courant
'''
# Principe: communication par "pipe" entre la commande 'ls' et le script python

import os
import subprocess

# lancement d'une commande unix qui s'execute dans un sous-processus
# l'argument stdout est utile pour que le script python puisse lire les
# resultats (la sortie standard) de ce sous-processus
pipe = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)
# variante: pipe = subprocess.Popen('ls -a', shell=True, stdout=subprocess.PIPE)

# rem: par défaut, Popen renvoie les résultats en "byte string" (dans stdout.readline())
#      d'où l'emploi ds le script de la fonction decode() après readline ! 
# voir la version <ls_subprocess11.py> qui utilise le paramètre universal_newlines 
# dans le constructeur Popen pour changer ce comportement par défaut 

nbf = 0
ligne = pipe.stdout.readline().decode()
while ligne:           # on lit dans le "pipe" associé à la commande "ls -a"
    ligne = ligne[:-1] # on se debarrasse du \n de fin de ligne
    if os.path.isfile(ligne):
        print(ligne)
        nbf += 1  # nbf = nbf + 1
    ligne = pipe.stdout.readline().decode()

pipe.stdout.close()
print("Nombre de fichiers ordinaires: ", nbf)
exit()

# variante style "ensembliste" pour le parcours des lignes de resultat
for ligne in pipe.stdout:
    ligne = ligne[:-1] # on se debarrasse du \n de fin de ligne
    if os.path.isfile(ligne):
        print(ligne.decode())
        nbf += 1
