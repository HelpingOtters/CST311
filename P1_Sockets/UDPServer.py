'''
Ricardo Barbosa 
Date: May 3, 2020
Class: CST 311 
Description: The server receives the data and converts the characters to uppercase. 
The server sends the modified data to the client

'''

# socket module
from socket import *

# initialize variable
serverPort = 12000

# server creates a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# associate serverPort(12000) with UDP socket
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

# allow UDP to to recieve and process packets from clients
while True:
   # accepts client and creates new socket (connectionSocket) in the server
   message, clientAddress = serverSocket.recvfrom(2048)
   modifiedMessage = message.decode().upper()
   serverSocket.sendto(modifiedMessage.encode(), clientAddress)
   