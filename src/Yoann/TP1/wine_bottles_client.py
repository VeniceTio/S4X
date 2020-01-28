#! /usr/bin/python3
# Usage: ./wine_bottles_client.py nbBouteilles [ host ]


import sys
import random
from socket import *              # portable socket interface plus constants
serverHost = 'localhost'          # server name, or: 'starship.python.net'
serverPort = 50007

if len(sys.argv) > 2:
    serverPort = int(sys.argv[1])
    message = sys.argv[2]
    if len(sys.argv) > 3:
        serverHost = sys.argv[3]
else:
    print("Usage: ./wine_bottles_client.py port nbBouteilles [ host ]")
    exit(1)

sockobj = socket(AF_INET,SOCK_STREAM)
try:
    sockobj.connect((serverHost,serverPort))
except:
    sys.stderr.write("Service non disponible\n")
else:
    sockobj.send(str(int(random.random()*100)).encode())
    data = sockobj.recv(1024).decode()  # receive line from server: up to 1k
    print('{:s} bouteille(s) recue(s)'.format(data))
    sockobj.close()