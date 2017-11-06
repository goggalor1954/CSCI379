#James Roesemann
#CSCI379
#Project 1
#UDP server

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to recive"
while True:
 message, clientAddress=serverSocket.recvfrom(2048)
 modifiedMessage = message.upper()
 serverSocket.sendto(modifiedMessage, clientAddress)


# not on unix system. to kill a process using port 12000
#sudo lsof -i:12000
# thenk kill the porcess id with kill -9 pid
# ps -fA | grep python
# ps -fA | grep python
