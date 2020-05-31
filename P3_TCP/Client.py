# Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
# Team: 3
# Date: 06/09/2020
# Title: Client.py
# Description: This is the client program which will be connected to a server 
# using a TCP connection. This program will send a message to the server then
# will receive a response from the server. 

"""
Team 1 will write the client for the regular assignment

"""
from socket import *
# In your command prompt, type in hostname and press enter.
# What comes up is your computer's hostname

serverName = gethostname() 
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())

clientSocket.close()
