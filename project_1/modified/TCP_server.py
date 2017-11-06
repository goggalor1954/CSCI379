#James Roesemann
#CSCI379
#Project 1
#Modified TCP server

from socket import *
serverPort = 9999
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while True:
 connectionSocket, addr = serverSocket.accept()
 #put an if statment here.
 sentence = connectionSocket.recv(1024)
 modified = connectionSocket.recv(1024)
 capitalizedSentence = sentence.upper()
 connectionSocket.send(capitalizedSentence)
 connectionSocket.close()
