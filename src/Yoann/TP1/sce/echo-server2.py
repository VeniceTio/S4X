#!/usr/bin/python3
# echo-server2.py : variante de echo-serveur1.py
# while True avec un break => while data avec lecture de data avant la boucle et
#                             relecture en fin de boucle

"""
Server side: open a TCP/IP socket on a port, listen for a message from
a client, and send an echo reply; this is a simple one-shot listen/reply
conversation per client, but it goes into an infinite loop to listen for
more clients as long as this server script runs; the client may run on
a remote machine, or on same computer if it uses 'localhost' for server
"""

from socket import *                    # get socket constructor and constants
myHost = ''                             # '' = all available interfaces on host
myPort = 50007                          # listen on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM)       # make a TCP socket object
sockobj.bind((myHost, myPort))               # bind it to server port number
sockobj.listen(5)                            # listen, allow 5 pending connects

while True:                                  # listen until process killed
    connection, address = sockobj.accept()   # wait for next client connect
    print('Server connected by', address)    # connection is a new socket
    data = connection.recv(1024).decode()    # read first line on client socket
    while data:
        message = 'Echo=>' + data            # send a reply line to the client
        connection.send(message.encode())    # until eof when socket closed
        # connection.send(b'Echo=>' + data)      # idem que les 2 instructions precedentes
        data = connection.recv(1024).decode()    # read next line on client socket
    connection.close()
