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

nombrePing = 0
nombrePong = 0

class Ping(Thread) :
    def __init__(self):
        global nombrePing
        super().__init__()
        nombrePing+=1
    def run(self) :
        global nombrePing
        global Switch
        # global Cond_ping, Cond_pong
        sleep(random())
        Cond_ping.acquire()
        while (Switch == 1) :
            Cond_pong.wait() # en attente d'une notification de pong
        print("ping ...", end=' ')
        Switch = 1
        Cond_ping.notify()
        Cond_ping.release()
        nombrePing-=1

class Pong(Thread) :
    def __init__(self):
        global nombrePong
        super().__init__()
        nombrePong+=1
    def run(self) :
        global nombrePong
        global Switch
        # global Cond_ping, Cond_pong
        sleep(random())
        Cond_pong.acquire()
        while Switch == 0 :
            Cond_ping.wait() # en attente d'une notification de pong
        print("pong")
        Switch = 0
        Cond_pong.notify()
        Cond_pong.release()
        nombrePong-=1

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
