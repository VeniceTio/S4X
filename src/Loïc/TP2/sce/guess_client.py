#! /usr/bin/python3
# guess_client.py
from socket import *
from time import sleep
from sys import stderr

serverHost = 'localhost' ; serverPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
try:
    sockobj.connect((serverHost, serverPort))
except:
    stderr.write("Pb de connexion !\n")
    exit(1)
max = 1000  # nb max à deviner
bottom = 0
top = max + 1

data = 1
while data != 0:
    sleep(1) # 1 sec. de réflexion
    guess = (bottom + top) // 2 # division entière
    msg = "%4d" % guess # sur 4 positions (cause valeur max possible = 1000)
    sockobj.send(msg.encode())
    print('Send' + msg + " ")
    data = sockobj.recv(2).decode()
    if data:
        print('Received:', data)
        data = int(data)
        if data == -1: # number to guess is higher
            bottom = guess
        elif data == 1:
            top = guess
        elif data == 0:
            message = "Wanted number is %d\n" % guess
            print(message)
    else: # Pb de connexion (?)
        data = 0 # break
sockobj.close()
