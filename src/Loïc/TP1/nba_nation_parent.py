#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# nba_nation_parent.py


import os,sys,subprocess
pipe = subprocess.Popen(["nba_nation_subproc.py",sys.argv[1]], stdout=subprocess.PIPE, universal_newlines=True)