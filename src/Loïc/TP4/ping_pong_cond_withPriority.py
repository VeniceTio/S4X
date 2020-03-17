#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# ping_pong_cond_withPriority.py

# Script avec trous a completer
# ============================

""" Une partie de ping pong avec des variables <Condition> """

# N objets (threads) Ping et N objets(threads) Pong

from threading import Thread, Lock, Condition
from random import random
from time import sleep
from sys import argv, stderr


class Ping(Thread) :
    waiting = 0
    def __init__(self):
        super().__init__()
    def run(self) :
        global Switch
        # global Cond_ping, Cond_pong
        sleep(random())
        Cond_ping.acquire()
        # S'il y a déjà une personne dans la file d'attente, alors on se
        # retrouve à la suite de la file d'attente sans pouvoir lui passer devant.
        if(Switch == 1 or Ping.waiting > 0) :
            Ping.waiting+=1
            Cond_pong.wait() # en attente d'une notification de pong
            Ping.waiting-=1
        print("ping ...", end=' ')
        Switch = 1
        Cond_ping.notify()
        Cond_ping.release()

class Pong(Thread) :
    waiting = 0
    def __init__(self):
        super().__init__()
    def run(self) :
        global Switch
        # global Cond_ping, Cond_pong
        sleep(random())
        Cond_pong.acquire()
        # S'il y a déjà une personne dans la file d'attente, alors on se
        # retrouve à la suite de la file d'attente sans pouvoir lui passer devant.
        if (Switch == 0 or Pong.waiting > 0) :
            Pong.waiting+=1
            Cond_ping.wait() # en attente d'une notification de pong
            Pong.waiting-=1
        print("pong")
        Switch = 0
        Cond_pong.notify()
        Cond_pong.release()

# main thread
if argv[1:] : 	# si liste des parametres non vide
    N = int(argv[1])
else :
    N = 100 	# 100 ping pong par defaut

Switch = 0 # pour bloquer pong au depart
Mutex = Lock()
# nb: mutex commun, parametre des deux variables Conditions
Cond_ping = Condition(Mutex)
Cond_pong = Condition(Mutex)

# creation d'une liste de N threads ping ; chaque thread fait UN (seul) ping
Threads_ping = [ Ping() for i in range(N) ]
# creation d'une liste de N threads pong ; chaque thread fait UN (seul) pong
Threads_pong = [ Pong() for i in range(N) ]

for t in Threads_ping : t.start()
for t in Threads_pong : t.start()
for t in Threads_ping : t.join()
for t in Threads_pong : t.join()

print("\nFin de partie !")

# ___ note ___
# comme Cond_ping et Cond_pong sont bases sur le meme Mutex
# les instructions Cond_ping.acquire() et Cond_pong.acquire() sont completement
# interchangeables ! idem pour Cond_ping.release() et Cond_pong.release()
