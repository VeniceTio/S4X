#! /usr/bin/python3
# -*- coding: utf8 -*-
# daemon_night.py

""" daemon TIMER  """

import threading
import time

def clock(interval):
    """ fonction exécutée par le thread daemon qui fait office de timer """
    while True:
        time.sleep(interval)
        print("zzzzzzzzzzz..........\t\t%s" % time.ctime())

# main
t = threading.Thread(target=clock, args=(1,))
t.daemon = True	 # t.setDaemon(True)
t.start()

print("Endormissement")
for i in range(3): # dans ce pgme, seulement 3 cycles de sommeil
                    # pour que ca ne s'eternise pas
    # 1 cycle de sommeil : 90 mn en moyenne
    # 10 mn en vrai => 1 sec. dans le programme
    # 4 phases par cycle
    print("Cycle %i" %(i + 1))
    print("phase de sommeil leger")
    time.sleep(2.5)
    print("phase de sommeil lent profond")
    time.sleep(3.5)
    print("phase de sommeil paradoxal")
    time.sleep(2)
    print("phase intermediaire")
    time.sleep(1)
print("DRINGGG ! Reveil")
