#! /usr/bin/python3

import threading
import time

def daemon():
    print('daemon is starting')
    time.sleep(2)
    print('daemon is exiting')

def non_daemon():
    print('non daemon is starting')
    print('non daemon is exiting')

# main
d = threading.Thread(target=daemon)
d.daemon = True		# d.setDaemon(True)
t = threading.Thread(target=non_daemon)
d.start()
# time.sleep(0.1)
t.start()


d.join()

# _____________________________
# resultat d'execution:
# daemon is starting
# non daemon is starting
# non daemon is exiting
# _____________________________
# si on "decommente" d.join, on obtient:
# daemon is starting
# non daemon is starting
# non daemon is exiting
# daemon is exiting
