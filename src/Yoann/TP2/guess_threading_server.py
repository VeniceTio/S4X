#!/usr/bin/python3
# guess_server.py

"""
Server side: open a TCP/IP socket on a port, listen for a message from
a client, and send an echo reply; this is a simple one-shot listen/reply
conversation per client, but it goes into an infinite loop to listen for
more clients as long as this server script runs; the client may run on
a remote machine, or on same computer if it uses 'localhost' for server
"""
import threading
from socket import *  # get socket constructor and constants
from random import random


class devinette(threading.Thread):

    def __init__(self,max,connection, address):
        threading.Thread.__init__(self)

        self.daemon=True
        self.max = max
        self.connec = connection
        self.address = address


    def run(self):
        connect = self.connec
        to_be_guessed = int(self.max * random()) + 1
        print(('Number to guess is: %d' % to_be_guessed))

        data = connection.recv(4).decode()  # read data on client socket (up to 4 bytes)
        while data:
            print(self.address, data + " ")
            data = int(data)
            if data > to_be_guessed:
                response = 1
            elif data < to_be_guessed:
                response = -1
            else:
                response = 0
            msg = "%2d" % response
            # send a reply line to the client
            connect.send(msg.encode())  # until eof when socket closed
            data = connect.recv(4).decode()  # read data on client socket (up to 4 bytes)
        connect.close()


# main
max = 1000  # nb max to guess

myHost = ''  # '' = all available interfaces on host
myPort = 50007  # listen on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM)  # make a TCP socket object
sockobj.bind((myHost, myPort))  # bind it to server port number
sockobj.listen(5)  # listen, allow 5 pending connects

while True:  # listen until process killed
    print("Serveur en attente de connexion")
    connection, address = sockobj.accept()  # wait for next client connect
    print('Server connected by', address)  # connection is a new socket
    devinette(max,connection,address).start()





