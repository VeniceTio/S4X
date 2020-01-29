#!/usr/bin/python3

import sys
import time
from socket import *                    # get socket constructor and constants
myHost = ''                             # '' = all available interfaces on host
stock = 300                            # Il y a 300 bouteilles en stock au début par défaut
myPort = 50001

if len(sys.argv) > 1:                   # text from cmd line args 2..n
    myPort = int(sys.argv[1])
    if len(sys.argv) > 2:                   # text from cmd line args 2..n
        stock = int(sys.argv[2])
else:
    print("Usage: ./wine_bottles_server.py <port> [ stockBouteilles ]")
    exit(1)


sockobj = socket(AF_INET, SOCK_STREAM)       # make a TCP socket object
sockobj.bind((myHost, myPort))               # bind it to server port number
sockobj.listen(5)                            # listen, allow 5 pending connects
print('Serveur en attente de commande')
while stock > 0:                                  # listen until process killed
    connection, address = sockobj.accept()   # wait for next client connect
    print('')
    print('Serveur connecté par', address)    # connection is a new socket
    data = int(connection.recv(1024).decode())    # read first line on client socket
    if data >= 0:
        time.sleep(1)
        print('Commande de {:d} bouteille(s)'.format(data))
        if (stock-data) >= 0:
            message = data            # send a reply line to the client
            stock = stock-data
        else:
            message = stock
            stock = 0
        time.sleep(1)
        print('Reste en stock : {:d} bouteille(s)'.format(stock))
        time.sleep(1)
        connection.send(str(message).encode())    # until eof when socket closed
    connection.close()
sockobj.close()
