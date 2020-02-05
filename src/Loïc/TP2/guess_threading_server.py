#! /usr/bin/python3
# guess_server.py

from socket import *
from random import random
from threading import Thread



def deviser(max, address, connect):
    to_be_guessed = int(max * random()) + 1
    print('Number to guess for (\'%s\', %d) is: ' % address, to_be_guessed)
    data = connect.recv(4).decode()
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
        connect.send(msg.encode())
        data = connect.recv(4).decode()
    connect.close()
max = 1000
# nb max to guess
myHost = '' ; myPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)
print("Serveur en attente de connexion")
while True:
    connection, address = sockobj.accept()
    print('Server connected by', address)
    t = Thread(target=deviser, args=(max, address, connection))
    t.start()
