#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# nba_nation_parent.py

import os,sys,subprocess
from datetime import datetime
pipe = subprocess.Popen(['./nba_nation_subproc.py',sys.argv[1]], stdout=subprocess.PIPE)
annee_courante = datetime.now().year

ligne = pipe.stdout.readline().decode()
while ligne:
    nom, _ , club, annee_nais, _ = ligne.split(':')  # conversion de la chaine en tableau
    age = annee_courante - int(annee_nais)
    print(nom + ', ' + club + ', ' + str(age))
    ligne = pipe.stdout.readline().decode()