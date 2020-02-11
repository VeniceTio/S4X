#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# ping_pong1.py

# Programme avec TROUS !!

""" Un programme qui fait ping pong ping pong ... un certain nombre (N) de fois
    N threads ping et N threads pong """

# ____________________________________________________
# utilisation d'un verrou (mutex) et d'une variable d'etat "bascule"
#                                    (Ping_OK)
import sys
import threading
from time import sleep
from random import random


# import A COMPLETER


class ping:

    def __init__(self):
        self.t = threading.Thread(target=self.run)
        self.t.daemon = True

    def start(self):
        self.t.start()

    def join(self):
        self.t.join()

    def run(self):
        sleep(random())  # pour un ordre d'entree ds la boucle aleatoire
        # (en fct du thread)
        Mutex.acquire()
        print("ping ... ", end="")
        Ping_OK.release()


class pong:

    def __init__(self):
        self.t = threading.Thread(target=self.run)
        self.t.daemon = True

    def start(self):
        self.t.start()

    def join(self):
        self.t.join()

    def run(self):
        sleep(random())  # pour un ordre d'entree ds la boucle aleatoire
        # (en fct du thread)
        Ping_OK.acquire()
        print("pong")
        Mutex.release()


# main thread
if __name__ == '__main__':
    if sys.argv[1:]:  # si liste des parametres non vide
        N = int(sys.argv[1])
    else:
        N = 100  # 100 ping pong par defaut

    Ping_OK = threading.Semaphore(0)  # pour ne pas faire pong s'il manque un ping
    Mutex = threading.BoundedSemaphore(1)
    # creation d'une liste de N threads ping ; chaque thread fait UN (seul) ping
    Threads_ping = [ping() for i in range(N)]
    # creation d'une liste de N threads pong ; chaque thread fait UN (seul) pong
    Threads_pong = [pong() for i in range(N)]

    for t in Threads_ping: t.start()
    for t in Threads_pong: t.start()
    for t in Threads_ping: t.join()
    for t in Threads_pong: t.join()

    print("\nFin de partie !")

# NB: le mutex pourrait aussi etre un parametre des fonctions ping et pong
