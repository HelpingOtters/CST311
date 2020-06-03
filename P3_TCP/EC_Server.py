"""
Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
Team: 3
Date: 06/09/2020
Title: EC_Server.py
Description: Extra Credit Assignment. This server will act as the processing 
relay between to clients. That is, this server will receive two connections
from two different clients. Each client will then send a message to the other 
client via the server. Example Client X wants to send  message to Client Y. To
do so it has to go through the server first (X -> S -> Y)
"""



from socket import *
from threading import Thread

# This video talks about multithreaded servers https://www.youtube.com/watch?v=pPOBH21RnaA
# From Max: https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/

serverPort = 12000
# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET,SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    # I believe everything below this will need to be added processed in a thread.
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
