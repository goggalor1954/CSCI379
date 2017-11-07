#James Roesemann
#CSCI379
#Project 1
#Modified TCP server

#this program must be running before running TCP_client

from socket import *
#recives TCP traffic on port 9999
serverPort = 9999
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
# the socket listens for 2 trasnsmissons.
serverSocket.listen(2)
print 'The server is ready to receive'
while True:
 connectionSocket, addr = serverSocket.accept()
#sentence represnets the sent sentance. modifier represents the command to change the value of sentence. 
 sentence = connectionSocket.recv(1024)
 modifier = connectionSocket.recv(1024)

#depending on the value of modifier, perform the apropriate modification and return the modified string.
 if modifier == 'Upper':
  modifiedSentence = sentence.upper()
 if modifier == 'Lower':
  modifiedSentence = sentence.lower()
 if modifier == 'Swap':
  modifiedSentence = sentence.swapcase()
 if modifier == 'Cap':
  modifiedSentence = sentence.capitalize()
 if modifier == 'Rev':
  modifiedSentence=' '.join(sentence.split(' ')[::-1])
#if a command wit hte value KILL is recived, transmit a message stating the the server has been killed and close the socket.
 if modifier == 'KILL':
  connectionSocket.send('Server killed.')
  connectionSocket.close()
  break
# if the value of modifier is not a valid commant, transmit a string indicationg that the user has entered an invalid command.
 if modifier not in {'Upper', 'Lower', 'Swap', 'Cap', 'Rev', 'KILL'}:
  modifiedSentence = 'You typed an invalid command.'
 connectionSocket.send(modifiedSentence)
