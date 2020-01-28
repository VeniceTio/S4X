#!/usr/bin/python3

import sys
from socket import *                    # get socket constructor and constants
host = ''
stock = 300

if len(sys.argv) > 1:
    port = int(sys.argv[1])
    if len(sys.argv) > 2:
        stock = int(sys.argv[2])
else:
    print("Usage: ./wine_bottles_server.py port [ stockBouteilles ]")
    exit(1)


sockobj = socket(AF_INET,SOCK_STREAM)
sockobj.bind((host,port))
sockobj.listen(5)

while stock > 0:
    print('\nServeur en attente de commande ')
    connection, address = sockobj.accept()
    print('Server connected by ', address)
    data = connection.recv(1024).decode()
    data = int(data)
    if data:
        print('Commande de {:d} bouteille(s) '.format(data))
        if (stock - data) >= 0:
            message = data
            stock = stock - data
        else:
            message = stock
            stock = 0
        print('Reste en stock : {:d} bouteille(s) '.format(stock))
        connection.send(str(message).encode())
    connection.close()
print('\n PLUS DE STOCK !\n')
sockobj.close()

