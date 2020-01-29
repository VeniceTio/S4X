#! /usr/bin/python3
# usage: ./echo-client.py [ host [ word ...]  ] 

"""
Client side: use sockets to send data to the server, and print server's
reply to each message line; 'localhost' means that the server is running
on the same machine as the client, which lets us test client and server
on one machine;  to test over the Internet, run a server on a remote
machine, and set serverHost or argv[1] to machine's domain name or IP addr;
Python sockets are a portable BSD socket interface, with object methods
for the standard socket calls available in the system's C library;
"""

import sys
from socket import *              # portable socket interface plus constants
serverHost = 'localhost'          # server name, or: 'starship.python.net'
serverPort = 50007                # non-reserved port used by the server

# message = [b'Hello network world']  
message = []
for x in ['Hello','network', 'world']:   # default text to send to server
    message.append(x.encode())

if len(sys.argv) > 1:
    serverHost = sys.argv[1]                # server from cmd line arg 1
    if len(sys.argv) > 2:                   # text from cmd line args 2..n
        message = []
        for x in sys.argv[2:]: 
            message.append(x.encode())

sockobj = socket(AF_INET, SOCK_STREAM)      # make a TCP/IP socket object
try:
    sockobj.connect((serverHost, serverPort))   # connect to server machine + port
except:  # variante: except error:
    sys.stderr.write("Echec connexion\n")
else:
    for line in message:
        sockobj.send(line)                  # send line to server over socket
        data = sockobj.recv(1024).decode()  # receive line from server: up to 1k
        print('Client received:', data)   

    sockobj.close()                         # close socket to send eof to server
