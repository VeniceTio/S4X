#! /usr/bin/python3
# -*- coding: utf8 -*-
# ___________________________________________________________
# Exemple pour montrer l'intérêt de verrouiller en ecriture
# une ressource critique (notion de section critique)
#
# Mettre en commentaire les instructions lock.acquire et
# lock.release qui protègent la mise à jour du compteur
# que constate t-on ? (valeur du compteur affichée)

from threading import Thread, Lock

# variables globales
compteur = 0
lock = Lock()

def incremente() :
    """ incremente valeur du compteur """
    global compteur
    for i in range(5000 * 1000): 	# 5 millions
        lock.acquire()
        compteur += 1 # en section critique
        lock.release()

thread1 = Thread(target=incremente)
thread2 = Thread(target=incremente)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("valeur du compteur", compteur)

