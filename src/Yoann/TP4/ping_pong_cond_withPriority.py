#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# ping_pong_cond.py

# Script avec trous a completer
# ============================

""" Une partie de ping pong avec des variables <Condition> """

# N objets (threads) Ping et N objets(threads) Pong

from threading import Thread, Lock, Condition
from random import random
from time import sleep
from sys import argv, stderr

class Ping(Thread) :
    def __init__(self, id):
        super().__init__()
        self.waiting = id
    def run(self) :
        global Switch
        global grp
        # global Cond_ping, Cond_pong
        sleep(random())
        Cond_ping.acquire()
        while grp !=self.waiting or Switch == 1:
            Cond_pong.wait() # en attente d'une notification de pong
        print("ping ...", end=' ')
        Switch = 1
        Cond_ping.notify_all()
        Cond_ping.release()

class Pong(Thread) :
    def __init__(self, id):
        super().__init__()
        self.waiting = id
    def run(self) :
        global Switch
        global grp
        # global Cond_ping, Cond_pong
        sleep(random())
        Cond_pong.acquire()  # idem => Cond_ping.acquire()
        while grp !=self.waiting or Switch == 0:
            Cond_ping.wait()  # en attente d'une notification de ping
        print("pong")
        Switch = 0
        grp += 1
        Cond_pong.notify_all()
        Cond_pong.release()

# main thread
if argv[1:] : 	# si liste des parametres non vide
    N = int(argv[1])
else :
    N = 100 	# 100 ping pong par defaut

grp = 0
Switch = 0 # pour bloquer pong au depart
Mutex = Lock()
# nb: mutex commun, parametre des deux variables Conditions
Cond_ping = Condition(Mutex) ; Cond_pong = Condition(Mutex)

Threads_ping = [ Ping(i) for i in range(N) ]
Threads_pong = [ Pong(i) for i in range(N) ]
for t in Threads_ping: t.start()
for t in Threads_pong: t.start()
for t in Threads_ping : t.join()
for t in Threads_pong : t.join()


print("\nFin de partie !")

# ___ note ___
# comme Cond_ping et Cond_pong sont bases sur le meme Mutex
# les instructions Cond_ping.acquire() et Cond_pong.acquire() sont completement
# interchangeables ! idem pour Cond_ping.release() et Cond_pong.release()
