#James Roesemann
#CSCI379
#Project 1
#Modified TCP server

from socket import *
serverPort = 9999
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
print 'The server is ready to receive'
while True:
 connectionSocket, addr = serverSocket.accept()
 sentence = connectionSocket.recv(1024)
 modifier = connectionSocket.recv(1024)

 if modifier == 'Upper':
  modifiedSentence = sentence.upper()
 if modifier == 'Lower':
  modifiedSentence = sentence.lower()
 if modifier == 'Swap':
  modifiedSentence = sentence.swapcase()
 if modifier == 'Cap':
  modifiedSentence = sentence.capitalize() ## also sets the other letters to lower case.
 if modifier == 'Rev':
  modifiedSentence=' '.join(sentence.split(' ')[::-1])
 if modifier == 'KILL':
  connectionSocket.send('Server killed.')
  connectionSocket.close()
  break
 if modifier not in {'Upper', 'Lower', 'Swap', 'Cap', 'Rev', 'KILL'}:
  modifiedSentence = 'You typed an invalid command.'
 connectionSocket.send(modifiedSentence)
