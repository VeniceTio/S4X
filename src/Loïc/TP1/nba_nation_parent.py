#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# nba_nation_parent.py


import os,sys,subprocess
pipe = subprocess.Popen(["./nba_nation_subproc.py",sys.argv[1]], stdout=subprocess.PIPE, universal_newlines=True)
annee_courante = datetime.now().year

ligne = pipe.stdout.readline()
while ligne:
    ligne = ligne[:-1]
    nom, _ , club, annee_nais, _ = un_joueur.split(':')  # conversion de la chaine en tableau
    age = annee_courante - int(annee_nais)
    print(nom + ', ' + club + ', ' + str(age))
