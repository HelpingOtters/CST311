# Name: Dan Sedano
# Date: 05/04/2020
# Title: TCP Server
# Description: This is a simple TCP server socket which receives a message from
# the client and then converts the string to upper case letters and sends the 
# messag back to the client

from socket import *

serverPort = 12000

# Creates socket (welcome socket) with IPv4 Protocol (AF_INET) TCP Protocol (Sock_STREAM).
serverSocket = socket (AF_INET, SOCK_STREAM)
# Assigns a port number to the socket and does not assign an IP address.
# Therefore, any client that sends a message to this port will be accepted.
serverSocket.bind(('', serverPort))
# Makes the socket ready to accept a connections. 
# The parameter (1) specifies the max queue of connections.
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    # Returns a connection socket object and the address of the bound socket from the client.
    connectionSocket, add = serverSocket.accept()
    # Receives the message from the client and decodes the message
    sentence = connectionSocket.recv(1024).decode()
    # Processes the message
    capitalizedSentence = sentence.upper()
    # Encodes the message and then sends back to client
    connectionSocket.send(capitalizedSentence.encode())
    # Closes the connection
    connectionSocket.close()