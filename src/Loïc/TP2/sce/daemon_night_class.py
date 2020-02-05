#! /usr/bin/python3
# -*- coding: utf8 -*-
# daemon_night_class.py

# version avec classe Clock héritant de Thread
""" daemon TIMER  """

import threading
import time

class Clock(threading.Thread):
    """ thread daemon qui fait office de timer """
    def __init__(self, interval):
        threading.Thread.__init__(self)
        # super(Clock, self).__init__()
        self.daemon = True		# self.setDaemon(True)
        self._interval = interval
    def run(self):
        while True:
            time.sleep(self._interval)
            print("zzzzzzzzzzz..........\t\t%s" % time.ctime())

# main
Clock(1).start()

print("Endormissement")
for i in range(3): # dans ce pgme, seulement 3 cycles de sommeil
                    # pour que ca ne s'éternise pas 
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

