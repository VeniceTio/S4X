#! /usr/bin/python3
# -*- coding: utf8 -*-
# bottles_of_beer.py

# Version utilisant os.read(descripteur_pour_lire, nbre de caracteres a lire)
#   Selon la longueur de la ligne :
#     verse = os.read(pipein, 118)
#     verse = os.read(pipein, 129)

import os
from time import sleep

def child(pipeout):
    bottles = 99
    bob = "bottles of beer"
    otw = "on the wall"
    take1 = "Take one down and pass it around"
    store = "Go to the store and buy some more"
    while True:
        if bottles > 0:
            values =  (bottles, bob, otw, bottles, bob, take1, bottles - 1, bob, otw)
            verse = "{0:2d} {1:s} {2:s},\n{3:2d} {4:s}.\n{5:s},\n{6:2d} {7:s} {8:s}.\n".format(*values)
            # variante:
            # verse = "%2d %s %s,\n%2d %s.\n%s,\n%2d %s %s.\n" % values

            bottles -= 1
        else:
            bottles = 99
            values =  (bob, otw, bob, store, bottles, bob, otw)
            verse = "No more {0:s} {1:s},\nno more {2:s}.\n{3:s},\n{4:2d} {5:s} {6:s}.\n".format(*values)
            # verse = "No more %s %s,\nno more %s.\n%s,\n%2d %s %s.\n" % values

        verse = str.encode(verse) # conversion string => byte object (nécessaire pour write !)
        # variante: verse = verse.encode()
        os.write(pipeout, verse)

def parent(pipein):
    counter = 1
    verse = os.fdopen(pipein)
    while True:
        print('verse {:d}'.format(counter))
        for i in range(0,4):
            line = verse.readline()
            line = line[:-1]
            print('{:s}'.format(line))
        print('')
        sleep(0.2) # pour avoir le temps de lire  :-)
        counter += 1
    verse.close()

# main
pipein, pipeout = os.pipe()
  # pipein => descripteur pour lire ce qui est en sortie du "pipe"
  # pipeout : descripteur pour ecrire (envoyer) dans le "pipe"
if os.fork() == 0: # processus fils
    os.close(pipein) # fermeture du descripteur que le processus n'utilise pas
    # en fait dans ce programme, la fermeture précédente n'est pas indispensable !
    # (car les 2 process bouclent à l'infini) mais c'est une bonne habitude a prendre !

    child(pipeout)
else:	# processus parent
    os.close(pipeout) # fermeture du descripteur que le processus n'utilise pas
    # en fait dans ce programme, la fermeture précédente n'est pas indispensable !
    # (car les 2 process bouclent à l'infini) mais c'est une bonne habitude à prendre !

    parent(pipein)
