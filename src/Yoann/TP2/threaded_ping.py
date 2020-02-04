#!/usr/bin/python3
# -*- coding: utf8 -*-
# threaded_ping.py host ...

# NB : c'est le shell qui affiche les lignes de la cde ping
#      (le script python n'intercepte pas les lignes de résultat, mais seulemt le code retour)

from sys import argv, stdin, stdout, stderr
from subprocess import call, DEVNULL 
from os.path import basename
from threading import Thread, Lock

def ping(hote, delai):
    # on lance la cde unix ping pour interroger hote
    # (option -w pour arrêter apres un certain délai sinon ping "boucle")

    retour = call(['/bin/ping', '-w' + str(delai), hote])  
             # cde 'ping' lancée ds un sous-processus et en avant-plan

    # Si on ne souhaite pas de trace du déroulement de ping (ni message d'erreur)
    # retour = call(['ping', '-w' + str(delai), hote], stdout=DEVNULL, stderr=DEVNULL) 

    etoiles = '*' * 20
    # =============================================================
    # REM : pour garantir l'atomicité des print, il faudrait protéger la section 
    #      qui suit par un verrou (Lock dans le module threading)
    # =============================================================

    mutex.acquire()
    print(etoiles)
    if retour == 0: 
        print(hote, ': VIVANT')
    elif retour == 1: 
        print(hote, ': DEFAILLANT ?')
    else:
        print(hote, ': INCONNU')
    print(etoiles)
    mutex.release()

# main
mutex = Lock()
if len(argv[1:]) == 0:
    stderr.write('Usage: ' + basename(argv[0]) + ' host ...\n')
    exit(1)
delai = 3
for hote in argv[1:]:
    t = Thread(target=ping, args=(hote, delai))
    t.start()
