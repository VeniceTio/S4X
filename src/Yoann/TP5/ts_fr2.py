#! /usr/bin/python3
# -*- coding: UTF-8 -*-
# ts_fr1.py
# auteurs (noms/prénoms) :
# - LOUAZEL Yoann,
# - GROSS Loïc,
# - TRITSCHBERGER Antoine
# - FÉLIX Antoine.

# section des import
from threading import Thread, BoundedSemaphore, Semaphore
from queue import Queue
from time import sleep
from random import random, uniform, randint


class Teenager(Thread):
    # variables de classe
    counter = 0
    enter_mutex = BoundedSemaphore(1)  # ou Semaphore(1)
    working = 0  # en train de faire une activité
    work_mutex = Semaphore(1)

    def __init__(self, num):
        super().__init__()
        self.__num = num

    def run(self):  # global NoOppositeCategory, WorkingMultiplex
        sleep(uniform(1, 20))
        Fifo.put('Teenager {:d} arrive'.format(self.__num))

        Teenager.enter_mutex.acquire()
        if Senior.counter != 0 or Teenager.counter == 0:
            NoOppositeCategory.acquire()
        Teenager.enter_mutex.release()

        self.enter()
        # début zone de code 'Activité' # nbre de places limité !
        WorkingMultiplex.acquire()

        Teenager.work_mutex.acquire()
        Teenager.working += 1
        Fifo.put('Teenager {:d}  s\'installe et bouge (compteur={:d})'.format(self.__num, Teenager.working))
        Teenager.work_mutex.release()

        sleep(uniform(1, 3))

        # fin zone de code 'Activité'
        Teenager.work_mutex.acquire()
        Teenager.working -= 1
        Fifo.put('Teenager {:d}  a fini son activité (compteur={:d})'.format(self.__num, Teenager.working))
        Teenager.work_mutex.release()

        WorkingMultiplex.release()  # un certain nombre d’instructions
        self.leave()

    def enter(self):
        Teenager.enter_mutex.acquire()
        Teenager.counter += 1
        Fifo.put('Teenager {:d} entre dans la salle'.format(self.__num))
        Teenager.enter_mutex.release()  # un certain nbre d’instructions

    def leave(self):  # on utilise aussi Teenager.enter_mutex
        Teenager.enter_mutex.acquire()
        Teenager.counter -= 1  # un certain nbre d’instructions
        if Teenager.counter == 0:
            NoOppositeCategory.release()
        Teenager.enter_mutex.release()


class Senior(Thread):
    # variables de classe
    counter = 0
    enter_mutex = Semaphore(1)  # = BoundedSemaphore(1)
    working = 0
    work_mutex = Semaphore(1)

    def __init__(self, num):
        super().__init__()
        self.__num = num

    def run(self):
        # global NoOppositeCategory, WorkingMultiplex
        sleep(uniform(1, 20))
        Fifo.put('Senior {:d} arrive'.format(self.__num))
        Senior.enter_mutex.acquire()
        if Teenager.counter != 0 or Senior.counter == 0:
            NoOppositeCategory.acquire()
        Senior.enter_mutex.release()

        self.enter()
        # début zone de code 'Activité' # nbre de places limité !
        WorkingMultiplex.acquire()

        Senior.work_mutex.acquire()
        # un certain nombre d’instructions
        Senior.working += 1
        Fifo.put('Senior {:d}  s\'installe et bouge (compteur={:d})'.format(self.__num, Senior.working))
        Senior.work_mutex.release()
        sleep(uniform(1, 3))

        # fin zone de code 'Activité'
        Senior.work_mutex.acquire()
        Senior.working -= 1
        Fifo.put('Senior {:d}  a fini son activité (compteur={:d})'.format(self.__num, Senior.working))
        Senior.work_mutex.release()

        WorkingMultiplex.release()  # un certain nombre d’instructions
        self.leave()

    def enter(self):
        Senior.enter_mutex.acquire()
        Senior.counter += 1
        Fifo.put('Senior {:d} entre dans la salle'.format(self.__num))
        Senior.enter_mutex.release()  # un certain nbre d’instructions

    def leave(self):  # on utilise aussi Senior.enter_mutex
        Senior.enter_mutex.acquire()
        Senior.counter -= 1  # un certain nbre d’instructions
        if Senior.counter == 0:
            NoOppositeCategory.release()
        Senior.enter_mutex.release()


class VIP(Thread):
    # variables de classe
    counter = 0
    enter_mutex = Semaphore(1)  # = BoundedSemaphore(1)
    working = 0
    work_mutex = Semaphore(1)

    def __init__(self, num):
        super().__init__()
        self.__num = num

    def run(self):
        # global NoOppositeCategory, WorkingMultiplex
        sleep(uniform(1, 20))
        Fifo.put('VIP {:d} arrive'.format(self.__num))

        NoOppositeCategory.acquire()

        self.enter()
        # début zone de code 'Activité' # nbre de places limité !
        VIP.work_mutex.acquire()
        # un certain nombre d’instructions
        VIP.working += 1
        Fifo.put('VIP {:d}  s\'installe et bouge (compteur={:d})'.format(self.__num, VIP.working))
        VIP.work_mutex.release()
        sleep(uniform(1, 3))

        # fin zone de code 'Activité'
        VIP.work_mutex.acquire()
        VIP.working -= 1
        Fifo.put('VIP {:d}  a fini son activité (compteur={:d})'.format(self.__num, VIP.working))
        VIP.work_mutex.release()
        self.leave()

    def enter(self):
        VIP.enter_mutex.acquire()
        VIP.counter += 1
        Fifo.put('VIP {:d} entre dans la salle'.format(self.__num))
        VIP.enter_mutex.release()  # un certain nbre d’instructions

    def leave(self):  # on utilise aussi Senior.enter_mutex
        VIP.enter_mutex.acquire()
        VIP.counter -= 1  # un certain nbre d’instructions
        NoOppositeCategory.release()
        VIP.enter_mutex.release()


class Printer(Thread):
    def __init__(self, fifo):
        Thread.__init__(self)
        self._fifo = fifo

    def run(self):
        item = self._fifo.get()  # get bloquant
        while item is not None:
            print(item)
            item = self._fifo.get()

    def stop_and_join(self):
        self._fifo.put(None)
        self.join()


# main thread
capacity = 5  # valeur par défaut
data = input(' Nbre de places pour bouger ? (5 par défaut: appuyer sur Enter) ')
if data: capacity = int(data)
how_many = int(input("Combien de clients ? "))

# variables globales
Fifo = Queue()
NoOppositeCategory = BoundedSemaphore(1)  # ou Semaphore(1)
WorkingMultiplex = BoundedSemaphore(capacity)  # pourrait aussi être une variable de classe
# de chacune des 2 classes Teenager et Senior
all_threads = []  # regroupe tous les threads (aussi bien Teenager que Senior)

teenagers = 0
seniors = 0
VIPs = 0
for i in range(how_many):
    s = randint(0, 2)  # on tire au sort la catégorie de client
    if s == 0:  # c’est un teenager
        teenagers += 1
        all_threads.append(Teenager(i + 1))
    elif s == 1:  # senior
        seniors += 1
        all_threads.append(Senior(i + 1))
    else:
        VIPs += 1
        all_threads.append(VIP(i + 1))

print(teenagers, "thread(s) Teenager")
print(seniors, "thread(s) Senior")
print(VIPs, "thread(s) VIP")
input("touche Enter pour démarrer")
print()
printer = Printer(Fifo)
printer.start()
for t in all_threads: t.start()
for t in all_threads: t.join()
printer.stop_and_join()
