#James Roesemann
#CSCI379
#Project 1
#Modified TCP client

import sys

from socket import *
serverName='127.0.0.1' #change this to the address of the server

if len(sys.argv)>1:
 serverName = sys.argv[1]


serverPort = 9999
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('Input sentence: ')
clientSocket.send(sentence)
command = raw_input('Type command Upper, Lower, Swap, Rev or Cap. Type KILL to kill the server process: ')
clientSocket.send(command)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
#this works, but if sentance and command get sent at the same time theres a chance that it won't be recived right. maybe sen it on diffrent ports? or diffrent identifiers.?
