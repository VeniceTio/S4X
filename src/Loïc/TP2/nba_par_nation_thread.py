#!/usr/bin/python3
# -*- coding: utf8 -*-
from os.path import basename, isfile
from datetime import datetime
from queue import Queue
from sys import argv, stderr, stdout
from time import sleep
from threading import Thread


# définition de la fonction writer
def producteur(fifo, joueurs):
    # parcours du fichier ligne apres ligne
    for un_joueur in joueurs:
        un_joueur = un_joueur[:-1] # on se débarrasse du '\n' de fin de ligne
        if un_joueur.endswith(nation):
            fifo.put(un_joueur, block = True)
    fifo.put(None, block = True)
    joueurs.close()

# définition de la fonction reader
def consommateur(fifo):
    sleep(1)
    annee_courante = datetime.now().year
    # get bloquant
    un_joueur = fifo.get(block = True)
    # idem que: un_joueur = fifo.get(block=True)
    while un_joueur is not None:
        # None: valeur spéciale ‘sentinelle’ prévue par le langage
        nom, _ , club, annee_nais, _ = un_joueur.split(':')  # conversion de la chaine en tableau
        age = annee_courante - int(annee_nais)
        print(nom + ', ' + club + ', ' + str(age))
        un_joueur = fifo.get() # get bloquant

# main
# lecture/contrôles des paramètres, ouverture du fichier
if len(argv[1:]) == 0:
    stderr.write("Usage: nba_par_nation.py nation\n")
    exit(1)
else:
    nation = argv[1]
file = "nba_2019.txt"
if not isfile(file):
    msg = file + " : Pb ouverture\n"
    stderr.write(msg)
    exit(1)

try:
    f = open(file, 'r') 	# f est un objet de type file
except IOError:
    sys.stderr.write(file + " : Pb ouverture\n")
# création de la file FIFO (Queue)
Fifo = Queue()
# Instanciation et démarrage des deux threads
t1 = Thread(target=producteur, args=(Fifo, f))
t2 = Thread(target=consommateur, args=(Fifo,)) # toujours mettre la virgule(,)
t1.start()
t2.start()
# fermeture du fichier
f.close()
