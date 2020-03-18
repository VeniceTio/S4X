#! /usr/bin/python3
# -*- coding: UTF-8 -*-
# boat_shuttle1.py

# SQUELETTE a completer !

# N threads Resident, un thread Boat et un thread dédié à l'affichage

# import
from threading import Thread, BoundedSemaphore, Semaphore
from queue import Queue
from time import sleep
from random import random, uniform, randint

# saisies
DefRiverainsValue = 5
try:
    NbResidents = input('Nbre de riverains ? (5 par defaut: taper Entree) ')
    if NbResidents == "":
        NbResidents = DefRiverainsValue
    else:
        NbResidents = int(NbResidents)
    Capacity = int(input('Capacite du bateau ? '))
    assert (NbResidents > 0)
    assert (Capacity > 0)
except ValueError:
    print('Nombre entier requis !')
    exit(1)
except AssertionError:
    print('Nbre (places et clients) positif requis !')
    exit(1)
print("===========================\n")


class Common:
    # variables communes à Resident et Boat
    mutex = BoundedSemaphore(1)
    boarders = 0
    boat = Semaphore(0)  # devient vrai pour un riverain lorsque le bateau arrive
    allAboard = Semaphore(0)  # vrai si "tt le monde" est à bord
    aboard = 0


class Resident(Thread):
    # variables de classe (static)
    multiplex = Semaphore(Capacity)

    def __init__(self, numero, fifo):
        super().__init__()
        self._numero = numero
        self._fifo = fifo

    def run(self):
        self.arrive()  # pour "espacer" les arrivees

        Resident.multiplex.acquire()
        # entre ds la zone d'embarquement du bateau dans la limite de la capacité (du bateau)
        item = 'Riverain {:d} arrive \nRiverain {:d} dans la zone d\'embarquement'.format(self._numero, self._numero)
        self._fifo.put(item)
        with Common.mutex:  # un riverain ne passe pas cette barrière si le bateau est a quai
            Common.boarders += 1
            item = 'Riverain {:d} pourra monter ds le prochain bateau'.format(self._numero)
            self._fifo.put(item)
        # attend signal pour pouvoir embarquer
        Common.boat.acquire()

        # Les riverains montent ds le bateau l'un après l'autre (pas de parallélisme)
        self.boardBoat()
        Common.aboard += 1  # pour savoir combien sont deja à bord
        Common.boarders -= 1
        Resident.multiplex.release()
        if Common.boarders != 0:
            Common.boat.release()
        else:
            Common.allAboard.release()

    def boardBoat(self):
        item = 'Riverain {:d} monte a bord'.format(self._numero)
        self._fifo.put(item)
        sleep(random())  # un certain temps(moins d'1 sec.) pour monter ds le bateau

    def arrive(self):
        # global NbResidents
        sleep(randint(0, NbResidents))
        # sleep(randint(0, 2 * NbResidents)) # si on veut espacer davantage les arrivees
        # (bateau qui roule parfois à vide)
        # sleep(randint(0, NbResidents // 4)) # si on veut plus d'encombrement
        item = 'Riverain {:d} arrive'.format(self._numero)
        self._fifo.put(item)


class Boat(Thread):
    def __init__(self, fifo):
        super().__init__()
        self._fifo = fifo
        self._fin = False

    def run(self):
        self._fin = False
        while not self._fin:
            sleep(randint(0, 1))
            # le bateau arrive
            item = 'Le bateau arrive [ {:d} riverain.s pouvant monter]'.format(Common.boarders)
            item = '{:50s} ____________'.format(item)
            self._fifo.put(item)
            with Common.mutex:
                if Common.boarders > 0:
                    Common.boat.release()  # délivre un Resident en attente à l'arrêt
                    Common.allAboard.acquire()

            self.depart()
            Common.aboard = 0

    def depart(self):
        item = 'Le bateau demarre avec {:d} passager.s'.format(Common.aboard)
        item = '{:50s} ++++++'.format(item)
        self._fifo.put(item)
        sleep(2)  # le temps du trajet jusqu'au lieu de débarquement
        item = "Debarquement des passagers (s'il y en a)"
        self._fifo.put('{:50s} ______'.format(item))

    def stop_and_join(self):
        self._fin = True
        self.join()


class Printer(Thread):
    def __init__(self, fifo):
        Thread.__init__(self)
        self._fifo = fifo
        self.setDaemon(True)

    def run(self):
        while True:
            print(Fifo.get())
            Fifo.task_done()
            sleep(0.1)


# main
Fifo = Queue()
Th_Resident = [Resident(i + 1, Fifo) for i in range(NbResidents)]
Th_Boat = Boat(Fifo)
Printer(Fifo).start()
Th_Boat.start()
for t in Th_Resident: t.start()
for t in Th_Resident: t.join()
Th_Boat.stop_and_join()
Fifo.join()
print("\nLe capitaine peut dormir!")
