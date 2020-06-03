"""
Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
Team: 3
Date: 06/09/2020
Title: EC_Client.py
Description: Extra Credit Assignment. This client will establish a TCP connection
to the server. It will then send a message to the server to be relayed to another
client. 
"""
# team 2

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




