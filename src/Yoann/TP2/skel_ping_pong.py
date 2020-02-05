#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# ping_pong1.py

# Programme avec TROUS !!

""" Un programme qui fait ping pong ping pong ... un certain nombre (N) de fois
    N threads ping et N threads pong """

#____________________________________________________
# utilisation d'un verrou (mutex) et d'une variable d'etat "bascule"
#                                    (Ping_OK)
import sys
import threading
from time import sleep
from random import random
# import A COMPLETER

def ping() :
    global Mutex  # pas obligatoire
    global Ping_OK  # obligatoire car la variable est m.a.j.
    sleep(random()) # pour un ordre d'entree ds la boucle aleatoire
                    # (en fct du thread)
    # A COMPLETER
    fin = True
    while (fin):
        Mutex.acquire()
        if not Ping_OK:
            Ping_OK = True
            print("ping ... ", end="")
            fin = False
        Mutex.release()

def pong() :
    global Mutex  # pas obligatoire
    global Ping_OK
    sleep(random()) # pour un ordre d'entree ds la boucle aleatoire
                    # (en fct du thread)
    # A COMPLETER
    fin = True
    while (fin):
        Mutex.acquire()
        if Ping_OK:
            Ping_OK = False
            print("pong")
            fin = False
        Mutex.release()

# main thread
if __name__ == '__main__' :
    if sys.argv[1:] : 	# si liste des parametres non vide
        N = int(sys.argv[1])
    else :
        N = 100 	# 100 ping pong par defaut

    Ping_OK = False     # pour ne pas faire pong s'il manque un ping
    Mutex = threading.Lock()
    # creation d'une liste de N threads ping ; chaque thread fait UN (seul) ping
    Threads_ping = [ threading.Thread(target=ping) for i in range(N) ]
    # creation d'une liste de N threads pong ; chaque thread fait UN (seul) pong
    Threads_pong = [ threading.Thread(target=pong) for i in range(N) ]

    for t in Threads_ping : t.start()
    for t in Threads_pong : t.start()
    for t in Threads_ping : t.join()
    for t in Threads_pong : t.join()

    print("\nFin de partie !")

# NB: le mutex pourrait aussi etre un parametre des fonctions ping et pong
