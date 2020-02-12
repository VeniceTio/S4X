#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# ping_pong1.py

# Programme avec TROUS !!

""" Un programme qui fait ping pong ping pong ... un certain nombre (N) de fois
    N threads ping et N threads pong """

#____________________________________________________
# utilisation d'un verrou (bSema) et d'une variable d'etat "bascule"
#                                    (Ping_OK)

from time import sleep
from random import random
import sys
from threading import Thread, Semaphore
from queue import Queue
# import A COMPLETER

# Pour compter le nombre de ligne : | wc -l

class Affiche(Thread):
    def __init__(self):
        Thread.__init__(self)   # Constructeur de la classe thread
        self.setDaemon(True)    # self.daemon=True Donc le thread se terminera quand le main se finira
    def run(self):
        while True:
            item = Fifo.get() # get bloquant
            print(item, end="")
            Fifo.task_done()


def ping() :
    sleep(random()) # pour un ordre d'entree ds la boucle aleatoire
                    # (en fct du thread)
    # A COMPLETER
    bSema.acquire()
    Fifo.put("ping...", block = True)
    bSema2.release()


def pong() :
    # global bSema  # pas obligatoire
    sleep(random()) # pour un ordre d'entree ds la boucle aleatoire
                    # (en fct du thread)
    # A COMPLETER
    bSema2.acquire()
    Fifo.put("pong\n", block = True)
    sleep(0.001) # Pour laisser le temps au thread daemon d'afficher
    bSema.release()


# main thread
if __name__ == '__main__' :
    if sys.argv[1:] : 	# si liste des parametres non vide
        N = int(sys.argv[1])
    else :
        N = 100 	# 100 ping pong par defaut

    Fifo = Queue()
    affi = Affiche()
    bSema = Semaphore(1)
    bSema2 = Semaphore(0)
    # creation d'une liste de N threads ping ; chaque thread fait UN (seul) ping
    Threads_ping = [ Thread(target=ping) for i in range(N) ]
    # creation d'une liste de N threads pong ; chaque thread fait UN (seul) pong
    Threads_pong = [ Thread(target=pong) for i in range(N) ]

    affi.start()
    for t in Threads_ping : t.start()
    for t in Threads_pong : t.start()
    for t in Threads_ping : t.join()
    for t in Threads_pong : t.join()
    print("\nFin de partie !")

# NB: le bSema pourrait aussi etre un parametre des fonctions ping et pong
