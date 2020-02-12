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
from queue import Queue
from time import sleep
from random import random

class Affiche(threading.Thread):
    def run(self):
        item = Fifo.get()   # get bloquant
        while not (item is None):   # while item is not None
            print(item, end="")
            sleep(0.001)  # courte pause (vous pouvez augmenter la durée si ça vous détend ;-)
            item = Fifo.get() # get bloquant

def ping():
    sleep(random())  # pour un ordre d'entree ds la boucle aleatoire
    # (en fct du thread)
    Mutex.acquire()
    Fifo.put("ping ... ", block=True)
    Ping_OK.release()


def pong():
    sleep(random())  # pour un ordre d'entree ds la boucle aleatoire
    # (en fct du thread)
    Ping_OK.acquire()
    Fifo.put("pong\n",block = True)
    Mutex.release()


# main thread
if __name__ == '__main__':
    if sys.argv[1:]:  # si liste des parametres non vide
        N = int(sys.argv[1])
    else:
        N = 100  # 100 ping pong par defaut
    Fifo = Queue()

    affiche = Affiche()

    Ping_OK = threading.Semaphore(0)  # pour ne pas faire pong s'il manque un ping
    Mutex = threading.BoundedSemaphore(1)
    # creation d'une liste de N threads ping ; chaque thread fait UN (seul) ping
    Threads_ping = [threading.Thread(target=ping) for i in range(N)]
    # creation d'une liste de N threads pong ; chaque thread fait UN (seul) pong
    Threads_pong = [threading.Thread(target=pong) for i in range(N)]

    affiche.start()
    for t in Threads_ping: t.start()
    for t in Threads_pong: t.start()
    for t in Threads_ping: t.join()
    for t in Threads_pong: t.join()
    Fifo.put(None)
    affiche.join()

    print("\nFin de partie !")

# NB: le mutex pourrait aussi etre un parametre des fonctions ping et pong
