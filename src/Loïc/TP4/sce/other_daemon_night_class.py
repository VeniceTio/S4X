#! /usr/bin/python3
# -*- coding: UTF-8 -*-
# other_daemon_night_class.py
# version où la classe Clock n'hérite pas de la classe Thread
# a la préférence de D.Beazley (cf Python Cookbook ch 12 Concurrency) 

""" daemon TIMER  """

from threading import Thread
from time import sleep, ctime

class Clock:
    def __init__(self, interval):
        self.interval = interval
    def start(self):
        t = Thread(target=self.run) 
        t.daemon = True
        # thread daemon qui fait office de timer
        t.start()
    def run(self):
        while True:
            sleep(self.interval)
            print("zzzzzzzzzzz..........\t\t%s" % ctime())

c = Clock(1)
c.start()

print("Endormissement")
for i in range(3): # dans ce pgme, seulement 3 cycles de sommeil
                    # pour que ca ne s'eternise pas 
    # 1 cycle de sommeil : 90 mn en moyenne 
    # 10 mn en vrai => 1 sec. dans le programme
    # 4 phases par cycle
    print("Cycle %i" %(i + 1))
    print("phase de sommeil leger")
    sleep(2.5)
    print("phase de sommeil lent profond")
    sleep(3.5)
    print("phase de sommeil paradoxal")
    sleep(2)
    print("phase intermediaire")
    sleep(1)
print("DRINGGG ! Reveil")
