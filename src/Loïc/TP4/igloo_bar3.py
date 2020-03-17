#! /usr/bin/python3
# -*- coding: UTF-8 -*-
# igloo_bar1.py
# +++++++++++++++++++++++++
# Squelette à compléter !
# +++++++++++++++++++++++++

# Contrainte : Nbre de clients en train de  boire <= nbre de sièges ds le bar


from threading import Thread, BoundedSemaphore
from queue import Queue
from time import sleep
from random import random, uniform

# __ var. globales __
# nb : Seats doit être connu avant de pouvoir initialiser la variable de
#      classe <enter_mutex>

DefSeatsValue = 5 # valeur par défaut
try:
    Seats = input('Nbre de places ? (5 par defaut: taper Entree) ')
    if Seats == "":
        Seats = DefSeatsValue
    else:
        Seats = int(Seats)
    Nb_clients = int(input('Nbre de clients ? '))
    assert(Seats > 0)
    assert(Nb_clients > 0)
except ValueError:
    print('Nombre entier requis !')
    exit(1)
except AssertionError:
    print('Nbre (places et clients) positif requis !')
    exit(1)

class Client(Thread):
    # variables de classe
    drinking = 0
    drink_mutex = BoundedSemaphore(1) # pour protéger les maj du compteur <drinking>
    enter_mutex = BoundedSemaphore(1) # pour respecter la contrainte
    prio_mutex = BoundedSemaphore(1) # pour respecter la priorité

    def __init__(self, id, fifo):
        super().__init__()  # Thread.__init__(self)
        self._id = id
        self._fifo = fifo

    def run(self):
        self.to_arrive() # pour "espacer" les arrivees
        attente = False

        Client.drink_mutex.acquire()
        if Seats == Client.drinking:
            state = "doit attendre une place"
            item = "client {0:3d} {1:30s}".format(self._id, state)
            self._fifo.put(item)
            #Client.prio_mutex.acquire()
            #attente = True
        Client.drink_mutex.release()
        print("ok")
        Client.enter_mutex.acquire()
        print("pas ok")
        Client.drink_mutex.acquire()
        if Seats - 1 > Client.drinking:
            Client.enter_mutex.release()
        ###Client.enter_mutex.acquire()    # "zone" où il ne doit pas y avoir plus <Seats> consommateurs

        Client.drinking += 1
        Client.drink_mutex.release()
        state = "s'installe et boit"
        item = "client {0:3d} {2:30s} compteur = {1:d}".format(self._id, \
                                                 Client.drinking, state)
        self._fifo.put(item)
        if attente :
            #Client.prio_mutex.release()
            #attente = False


        # phase de consommation
        self.drink()

        # Sortie d'un client
        Client.drink_mutex.acquire()
        Client.drinking -= 1
        Client.drink_mutex.release()
        state = "quitte sa place"
        item = "client {0:3d} {2:30s} compteur = {1:d}".format(self._id, \
                                                 Client.drinking, state)
        self._fifo.put(item)
        Client.drink_mutex.acquire()
        if Seats - 1 == Client.drinking :
            Client.enter_mutex.release()
        Client.drink_mutex.release()


    def drink(self):
        sleep(uniform(1, 3))

    def to_arrive(self):
        #sleep(uniform(0, 20))
        sleep(uniform(0, Nb_clients // 2))
        item = 'client {:3d} arrive au bar'.format(self._id)
        self._fifo.put(item)

class Affiche(Thread):
    def __init__(self, fifo):
        super().__init__()  # Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            print(Fifo.get())

# main
Fifo = Queue()
affi = Affiche(Fifo)
Th_clients = [Client(i+1, Fifo) for i in range(Nb_clients)]
for t in Th_clients : t.start()
for t in Th_clients : t.join()
print("\nPlus de client !")
