#James Roesemann
#CSCI379
#Project 1
#UDP client

from socket import *
#serverName='hostname'
serverName='127.0.0.1' #change this to the address of the server
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('input lowercase sentance:')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()

