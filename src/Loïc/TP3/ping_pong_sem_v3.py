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
# import A COMPLETER

# Pour compter le nombre de ligne : | wc -l

class Ping():
    def __init__(self):
        self.t = Thread(target=self.run)
    def start(self):
        self.t.start()
    def run(self):
        sleep(random()) # pour un ordre d'entree ds la boucle aleatoire
                        # (en fct du thread)
        # A COMPLETER
        bSema.acquire()
        print("ping ... ", end="")
        bSema2.release()
    def join(self):
        self.t.join()


class Pong():
    def __init__(self):
        self.t = Thread(target=self.run)
    def start(self):
        self.t.start()
    def run(self):
        sleep(random()) # pour un ordre d'entree ds la boucle aleatoire
                        # (en fct du thread)
        # A COMPLETER
        bSema2.acquire()
        print("pong")
        bSema.release()
    def join(self):
        self.t.join()




# main thread
if __name__ == '__main__' :
    if sys.argv[1:] : 	# si liste des parametres non vide
        N = int(sys.argv[1])
    else :
        N = 100 	# 100 ping pong par defaut

    Ping_OK = False     # pour ne pas faire pong s'il manque un ping
    bSema = Semaphore(1)
    bSema2 = Semaphore(0)

    # creation d'une liste de N threads ping ; chaque thread fait UN (seul) ping
    Threads_ping = [ Ping() for i in range(N) ]
    # creation d'une liste de N threads pong ; chaque thread fait UN (seul) pong
    Threads_pong = [ Pong() for i in range(N) ]

    for t in Threads_ping : t.start()
    for t in Threads_pong : t.start()
    for t in Threads_ping : t.join()
    for t in Threads_pong : t.join()

    print("\nFin de partie !")

# NB: le bSema pourrait aussi etre un parametre des fonctions ping et pong
