#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#______________________________________________________________________________ 
# MULTI chronometre qui va creer un nouveau (processus) chrono chaque fois qu'il
# receptionne le signal SIGTERM (=15)
# A reception du signal SIGINT, le processus envoie ce signal vers tous ses 
# fils qui affichent chacun la valeur de leur compteur
# sur le signal SIGQUIT le processus envoie ce signal vers tous ses fils, qui 
# affichent la valeur de leur compteur et arretent.
#______________________________________________________________________________ 

import signal, os, sys

# gestionnaires d'evenements
def nouveau(signum, frame) :
    # creation d'un processus "chrono"
    try: pid = os.fork()
    except OSError: print('Fork: erreur !', file=sys.stderr)
    else: # fork OK
        if pid == 0 : 
        # le fils exec. le code de chrono.py qui "recouvre"/ecrase celui du pere
            os.execl('./chrono.py', " ")  # positionner droit x pour chrono.py !
            exit(255) # seulement fait si execl echoue
        else :
            FILS.append(pid)  # on ajoute le PID du fils "chrono"
            # verification
            print('*************************************')
            print('creation chrono de numero (', pid, ')')
            # print('creation chrono de numero (%d)' %pid)
            # print('creation chrono de numero ({0:d})'.format(pid))
            print('liste des fils', FILS)

def  inter(signum, frame) :
    # affiche la valeur du compteur de chaque chrono
    # on transmet ce signal vers tous les fils (ils savent s'afficher !)
    print('\nTransmission du signal SIGINT a tous les chronometres  fils \n')
    for pid in FILS :
        os.kill(pid, signal.SIGINT)

def arret(signum, frame) :
    print('\nTransmission du signal SIGQUIT a tous les chronometres  fils \n')
    for pid in FILS :
        os.kill(pid, signal.SIGQUIT)
    exit(0)

# debut du programme main
# association signaux/handlers 
signal.signal(signal.SIGTERM, nouveau)	# on cree un nouveau chrono
signal.signal(signal.SIGINT, inter)     # fct "inter" liee au signal SIGINT (2)
signal.signal(signal.SIGQUIT, arret)  	# fct "arret" liee au signal SIGQUIT (3)

monPID = os.getpid()
FILS = [] # pour memoriser PID des chronos
print("Je suis le gestionnaire de CHRONOMETRES !")
print("__________________")
print("kill -2", monPID, "(dans un terminal) pour affichage de tous les chronos")
print("kill -3", monPID, "(dans un terminal) pour quitter et stop chronometres")
print("kill -15", monPID, "(dans un terminal) pour creer un chrono") 
print("__________________")

# boucle attente evenements
while 1 : signal.pause() # attend reception d'un signal
