#!/usr/bin/python3
# -*- coding: utf8 -*-

from threading import Thread, Lock
from time import sleep
from sys import argv, stderr, stdout
from queue import Queue
from datetime import datetime
from os.path import basename


# définition de la fonction writer
def producteur(fifo, joueurs, nation):
    for un_joueur in joueurs:
        un_joueur = un_joueur[:-1]
        if un_joueur.endswith(nation):
            fifo.put(un_joueur)
            sleep(2)
    fifo.put(None)
    joueurs.close()

# définition de la fonction reader
def consommateur(fifo):
     annee_courante = datetime.now().year
     un_joueur = fifo.get() # get bloquant # idem que: un_joueur = fifo.get(block=True)
     while un_joueur is not None: # None: valeur spéciale ‘sentinelle’ prévue par le langage
         nom, _, club, annee_nais, _ = un_joueur.split(':')  # conversion de la chaine en tableau
         age = annee_courante - int(annee_nais)
         print(nom + ', ' + club + ', ' + str(age))
         un_joueur = fifo.get() # get bloquant

 # main
 # lecture/contrôles des paramètres, ouverture du fichier
nom_fichier = 'nba_2019.txt'
if len(argv[1:]) != 0:
    nation = argv[1]
else:
    stderr.write("Usage : " + basename(argv[0]) + " nation\n")
    exit(1)

try:
    joueurs = open(nom_fichier, 'r')
except IOError:
    msg = nom_fichier + ": Pb ouverture !\n"
    stderr.write(msg)
else:
    # création de la file FIFO (Queue)
    Fifo = Queue()
    # Instanciation et démarrage des deux threads
    thread1 = Thread(target=producteur, args=(Fifo,joueurs,nation))
    thread2 = Thread(target=consommateur, args=(Fifo,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    # fermeture du fichier
    joueurs.close()