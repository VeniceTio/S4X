#! /usr/bin/python3
# -*- coding: UTF-8 -*-
# igloo_bar1.py
# +++++++++++++++++++++++++
# Squelette à compléter !
# +++++++++++++++++++++++++

# Contrainte : Nbre de clients en train de  boire <= nbre de sièges ds le bar


from threading import Thread, BoundedSemaphore, Semaphore
from queue import Queue
from time import sleep
from random import random, uniform

# __ var. globales __
# nb : Seats doit être connu avant de pouvoir initialiser la variable de
#      classe <enter_multiplex>

DefSeatsValue = 5  # valeur par défaut
try:
    Seats = input('Nbre de places ? (5 par defaut: taper Entree) ')
    if Seats == "":
        Seats = DefSeatsValue
    else:
        Seats = int(Seats)
    Nb_clients = int(input('Nbre de clients ? '))
    assert (Seats > 0)
    assert (Nb_clients > 0)
except ValueError:
    print('Nombre entier requis !')
    exit(1)
except AssertionError:
    print('Nbre (places et clients) positif requis !')
    exit(1)


class Client(Thread):
    # variables de classe
    drinking = 0
    attente = 0
    alive = 0
    drink_mutex = Semaphore(1)  # pour protéger les maj du compteur <drinking>
    # enter_multiplex = BoundedSemaphore(1) # pour respecter la contrainte
    attente_mutex = Semaphore(0)

    def __init__(self, id, fifo):
        super().__init__()  # Thread.__init__(self)
        self._id = id
        self._fifo = fifo
        Client.alive +=1

    def run(self):
        self.to_arrive()  # pour "espacer" les arrivees
        Client.drink_mutex.acquire()
        if Client.drinking == Seats:
            Client.attente += 1
            text = "doit attendre une place car le bar est plein"
            state = "client {0:3d} {2:30s} compteur_attente = {1:d}".format(self._id, Client.attente, text)
            self._fifo.put(state)
            Client.drink_mutex.release()
            Client.attente_mutex.acquire()
            Client.attente -= 1
            Client.drink_mutex.release()
        elif Client.drinking == 0 and Client.attente == 0:
            Client.attente +=1
            text = "doit attendre une place car le bar est vide"
            state = "client {0:3d} {2:30s} compteur_attente = {1:d}".format(self._id, Client.attente, text)
            self._fifo.put(state)
            if Client.alive == 1:
                state = "Abandonne ! (pas de partenaire possible)"
                self._fifo.put(state)
                return
            Client.drink_mutex.release()
            Client.attente_mutex.acquire()
            Client.attente -= 1
        elif Client.drinking == 0 and Client.attente == 1:
            Client.attente_mutex.release()
            Client.drink_mutex.release()
        else:
            Client.drink_mutex.release()

        # "zone" où il ne doit pas y avoir plus <Seats> consommateurs
        Client.drink_mutex.acquire()
        Client.drinking += 1

        state = "s'installe et boit"
        item = "client {0:3d} {2:30s} compteur_cons = {1:d}".format(self._id, Client.drinking, state)
        self._fifo.put(item)
        Client.drink_mutex.release()

        # phase de consommation
        self.drink()

        # Sortie d'un client
        Client.drink_mutex.acquire()
        Client.drinking -= 1
        state = "quitte sa place"
        item = "client {0:3d} {2:30s} compteur_cons = {1:d}".format(self._id, Client.drinking, state)
        self._fifo.put(item)
        if Client.drinking <= Seats - 1:
            Client.alive -= 1
            if Client.attente > 0:
                Client.attente_mutex.release()
            else:
                Client.drink_mutex.release()

    def drink(self):
        sleep(uniform(1, 3))

    def to_arrive(self):
        sleep(uniform(0, 5))
        # sleep(uniform(0, Nb_clients // 2))
        item = 'client {:3d} arrive au bar'.format(self._id)
        self._fifo.put(item)


class Affiche(Thread):
    def __init__(self, fifo):
        super().__init__()  # Thread.__init__(self)
        self.setDaemon(True)

    def run(self):
        while True:
            print(Fifo.get())
            Fifo.task_done()
            sleep(0.1)


# main
Fifo = Queue()
Th_clients = [Client(i + 1, Fifo) for i in range(Nb_clients)]

Affiche(Fifo).start()
for t in Th_clients: t.start()
for t in Th_clients: t.join()
Fifo.join()

print("\nPlus de client !")
