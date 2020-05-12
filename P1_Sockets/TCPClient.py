# Name: Dan Sedano
# Date: 05/04/2020
# Title: TCP Client
# Description: This is a simple TCP client Socket which sends a lower case string to the 
# server client and receives a response and then decodes the response.


from socket import *
serverName = gethostbyname(gethostname()) # returns the host IP
serverPort = 12000
# Creates socket object with IPv4 Protocol (AF_INET) TCP Protocol (Sock_STREAM).
clientSocket = socket(AF_INET, SOCK_STREAM)
# Establishes connection with server (initiates 3-way handshake).
clientSocket.connect((serverName, serverPort))
# Asks for user input.
sentence = raw_input('Input lowercase sentence: ')
# Encodes the user input (String to Bytes) and transmits to server 
# via established TCP connection. 
# Note: no address needed for TCP.
clientSocket.send(sentence.encode())
# Receives encoded returned response from server.
modifiedSentence = clientSocket.recv(1024)
# Decodes modifiedSentence (Byte to String) and prints out to terminal.
print('From Server: ' + modifiedSentence.decode())
# Closes the socket.
clientSocket.close()
