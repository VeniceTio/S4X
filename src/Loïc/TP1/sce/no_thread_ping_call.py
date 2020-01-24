#!/usr/bin/python3
# -*- coding: utf8 -*-
# no_thread_ping_call.py host ...

# NB : c'est le SHELL qui affiche les lignes de la cde ping
#      (le script python n'intercepte pas les lignes de résultat, mais seulemt le code retour)

from sys import argv, stdin, stdout, stderr
from subprocess import call, DEVNULL
from os.path import basename

if len(argv[1:]) == 0:
    stderr.write('Usage: ' + basename(argv[0]) + ' host ...\n')
    exit(1)

delai = 3  # 3 sec.

for hote in argv[1:]:
    # on lance la cde unix ping pour interroger hote
    # (option -w pour arrêter apres un certain délai sinon ping "boucle")

    # nb: on récupère ds la variable <retour> le code retour de la cde ping
    #                                         (cad la valeur de $? du shell)

    retour = call(['/bin/ping', '-w' + str(delai), hote]) # commande 'ping' lancée ds un 
                                                          # sous-processus et en avant-plan
    # idem : retour = call('/bin/ping -w' + str(delai) + ' ' + hote, shell=True) 

    # __ si on ne veut pas de trace du déroulement de ping, ni message d'erreur__
    # retour = call(['ping', '-w' + str(delai), hote], stdout=DEVNULL, stderr=DEVNULL) 
    # __  __

    print('*' * 40) 
    if retour == 0: 
        print(hote, ': VIVANT')
    elif retour == 1: 
        print(hote, ': DEFAILLANT ?')
    else:
        print(hote, ': INCONNU')
    print('*' * 40)
