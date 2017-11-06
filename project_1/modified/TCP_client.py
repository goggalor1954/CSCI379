#James Roesemann
#CSCI379
#Project 1
#Modified TCP client

from socket import *
serverName='127.0.0.1' #change this to the address of the server
#serverName='hostname'
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('input sentence:')
command = raw_input('All upper, all lower, or something else')
clientSocket.send(sentence)
clientSocket.send(command)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
