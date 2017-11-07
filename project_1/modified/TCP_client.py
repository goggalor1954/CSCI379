#James Roesemann
#CSCI379
#Project 1
#Modified TCP client

#the TCP_server must be running before before this program runs.

import sys
from socket import *

#the default serverName is the loopback address
serverName='127.0.0.1'

# if this program is run with arguments the value of the first argumetn is assigned to serverName
# if no arguments are given the default serverName is the loopback address.
# if given an invalid or unreachable ip address as an argument the program will not run.
if len(sys.argv)>1:
 serverName = sys.argv[1]

#sends TCP traffic on port 9999
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# the first line intered is considered the sentance. the second line entered is considered the command. bolth are sent to the server.
sentence = raw_input('Input sentence: ')
clientSocket.send(sentence)

# The valid commands are 
# Upper: changes all letters in the string to upper case.
# Lower: changes all letters in the string to lower case.
# Swap: Change all the upper case letters to lower case letters and change all the lower case letters to uppercase letters.
# Rev: reverse the order of the words in the string.
# Cap: capitlize the first letter of the string. change all other letters to lower case.
# KILL: Kills the process running on the server. Returns a message confirming this.
command = raw_input('Type command Upper, Lower, Swap, Rev or Cap. Type KILL to kill the server process: ')
clientSocket.send(command)

#if both sentance and command were transmited and considered valid, the server performs the command transformation and returns a string. We then print the string.
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()

