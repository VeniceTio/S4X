#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# usage: nba_par_nation nation

import os,sys,datetime
if len(sys.argv[1:]) == 0:
    sys.stderr.write("Usage: nba_par_nation.py nation\n")
    exit(1)
file = "nba_2019.txt"
if not os.path.isfile(file):
    msg = file + " : Pb ouverture\n"
    sys.stderr.write(msg)
    exit(1)

try:
    f = open(file, 'r') 	# f est un objet de type file
except IOError:
    sys.stderr.write(file + " : Pb ouverture\n")
else:  				# si ouverture ok
# parcours du fichier ligne apres ligne
    for line in f:
        splitline = line.split(':')
        if splitline[-1][:-1] == sys.argv[1]:
            age = datetime.date.today().year - int(splitline[-2])
            chaine = splitline[0]
            while len(chaine) < 30 :
                chaine += " "
            chaine += "| " + splitline[2]
            while len(chaine) < 60 :
                chaine += " "
            chaine += "| " + str(age)
            print(chaine)

    f.close()
