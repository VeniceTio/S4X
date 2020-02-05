#! /usr/bin/python3
# guess_server.py

from socket import *
from random import random

def deviser(max):
    to_be_guessed = int(max * random()) + 1
    print(('Number to guess is: %d' % to_be_guessed))
    data = connection.recv(4).decode()
    while data:
        print(data + " ")
        data = int(data)
        if data > to_be_guessed:
            response = 1
        elif data < to_be_guessed:
            response = -1
        else:
            response = 0
        msg = "%2d" % response
        # send a reply line to the client
        connection.send(msg.encode())
        data = connection.recv(4).decode()
max = 1000
# nb max to guess
myHost = '' ; myPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)
while True:
    print("Serveur en attente de connexion")
    connection, address = sockobj.accept()
    print('Server connected by', address)
    deviser(max)
    connection.close()
