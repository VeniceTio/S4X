#!/usr/bin/python3
# chrono.py
# _____________________________________________________
# creation d'un processus chrono qui compte les secondes
# sur le signal SIGINT ( CTRL C) le processus affiche la valeur du compteur
# sur le signal SIGQUIT ( CTRL \ ) le processus affiche le compteur et quitte.
# _____________________________________________________
# tester aussi le comportement du pgme en le lancant dans une fenetre et en 
# envoyant des signaux depuis une autre
# kill -2 pid pour declencher SIGINT
# kill -3 pid pour SIGQUIT

import os
from signal import signal, alarm, pause, SIGINT, SIGQUIT, SIGALRM

# gestionnaires d'evenements (handlers)
#_______________________________

def seconde(signum, frame) :
    global nsec  
    	# pour dire que c'est la variable <nsec> du "main"
        # sinon: variable locale (et modif valeur non visible ds le main !
    nsec += 1
    alarm(1)	# on repositionne l'evenement SIGALRM

def inter(signum, frame) :
    # affiche la valeur du compteur
    print("CHRONO (", PID, ") ->", nsec, "secondes") 
    # print('CHRONO (%d) -> %d secondes' %(PID, nsec))
    # print('CHRONO ({0:d}) -> {1:d} secondes'.format(PID, nsec))

def arret(signum, frame) :
    # affiche la valeur du compteur et quitte
    print(nsec, "secondes ecoulees")
    print("Fin du chronometre (", PID, ")")
    exit(0)

# debut du programme (principal)
# ____________________________

nsec = 0   # nbre de secondes
PID = os.getpid()

# association de fonctions (handlers) aux signaux
signal(SIGALRM, seconde) # on associe la fct "seconde" au signal SIGALRM(14)
signal(SIGINT, inter)    # le signal SIGINT (2) lancera "inter"
signal(SIGQUIT, arret)   # le signal SIGQUIT (3) lancera "arret"

alarm(1)  # on declenche l'alarme dans 1 seconde
print("CHRONO (", PID, ") demarre !")   # on affiche le pid
# print('CHRONO (%d) demarre !' %PID)
# print('CHRONO ({0:d}) demarre !'.format(PID))

# boucle infinie d'attente des evenements
while 1 : pause()	# en attente reception signal
