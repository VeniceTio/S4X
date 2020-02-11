#!/usr/bin/python3
# -*- coding: utf8 -*-
# no_thread_ping_Popen.py host ...

# NB : c'est le SHELL qui affiche les lignes de la cde ping
#      (le script python n'intercepte pas les lignes de résultat, mais seulemt le code retour)

from sys import argv, stdin, stdout, stderr
from subprocess import Popen, DEVNULL 
from os.path import basename

if len(argv[1:]) == 0:
    stderr.write('Usage: ' + basename(argv[0]) + ' host ...\n')
    exit(1)

delai = 3  # 3 sec.

for hote in argv[1:]:
    # on lance la cde unix ping pour interroger hote
    # (option -w pour arrêter apres un certain délai sinon ping "boucle")
    process = Popen(['/bin/ping', '-w' + str(delai), hote])  # cde 'ping' lancée ds un sous-processus
                                                             # et en arrière-plan !

    # Si on ne souhaite pas de trace du déroulement de ping (ni message d'erreur)
        # __ variante1 __
        # process = Popen(['/bin/ping', '-w' + str(delai), hote], stdout=DEVNULL, stderr=DEVNULL)
        # __ fin variante1 __

        # __ variante2 __
        # process = Popen('/bin/ping -w' + str(delai) + ' ' + hote + ' 1>/dev/null 2>&1', shell=True)
        # __ fin variante2 __

    retour = process.wait() # attente fin de la commande lancée par Popen et
                            # mémorisation code retour (valeur de $? du shell)	
    print('*' * 40)
    if retour == 0: 
        print(hote, ': VIVANT')
    elif retour == 1: 
        print(hote, ': DEFAILLANT ?')
    else:
        print(hote, ': INCONNU')
    print('*' * 40)

# _____ autre proposition au lieu de retour = process.wait() ____
#    process.communicate()
#    retour = process.returncode
