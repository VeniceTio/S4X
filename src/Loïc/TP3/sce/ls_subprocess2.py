#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# ls_subprocess2.py

''' Affichage des noms des fichiers reguliers (caches ou non)
              et du nombre de fichiers du repertoire courant
'''
# Principe: communication par "pipe" entre la commande 'ls' et le script python

from os.path import isfile
from subprocess import Popen, PIPE

# lancement d'une commande unix qui s'execute dans un sous-processus
# l'argument stdout est utile pour que le script python puisse lire les
# resultats (la sortie standard) de ce sous-processus
pipe = Popen(['ls', '-a'], stdout=PIPE)
# variante: pipe = Popen('ls -a', shell=True, stdout=PIPE)

nbf = 0
data, errors = pipe.communicate()
# ici, data est une chaine de la forme (en bytestring) 'fich1\nfich2\nfich avec esp ds nom\n ...'
# noter que la methode communicate rend disponible le code retour ($?) de
# la commande du shell, accessible par: pipe.returncode

# variante1: data = pipe.communicate()[0]
# variante2: data = pipe.stdout.read()

data = data.decode()    # conversion bytestring => Unicode string (sinon split echoue )
data = data.split('\n') # decoupage de la chaine et transformation en liste
for line in data:
    if isfile(line):
        print(line)
        nbf += 1

pipe.stdout.close()
print("Nombre de fichiers ordinaires: ", nbf)
