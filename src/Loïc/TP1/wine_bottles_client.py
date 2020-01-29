#! /usr/bin/python3
# Usage: ./wine_bottles_client.py nbBouteilles [ host ]


import sys
from socket import *              # portable socket interface plus constants
serverHost = 'localhost'          # server name, or: 'starship.python.net'


if len(sys.argv) > 2:                   # text from cmd line args 2..n
    serverPort = int(sys.argv[1])
    message = sys.argv[2]
    if len(sys.argv) > 3:
        serverHost = sys.argv[3]         # server from cmd line arg 1
else:
    print("Usage: ./wine_bottles_client.py <port> <nbBouteilles> [ host ]")
    exit(1)

sockobj = socket(AF_INET, SOCK_STREAM)      # make a TCP/IP socket object
try:
    sockobj.connect((serverHost, serverPort))   # connect to server machine + port
except:  # variante: except error:
    sys.stderr.write("Service non disponible\n")
else:
    sockobj.send(message.encode())                  # send line to server over socket
    data = sockobj.recv(1024).decode()  # receive line from server: up to 1k
    print('{:s} bouteille(s) recue(s)'.format(data))

    sockobj.close()                         # close socket to send eof to server
