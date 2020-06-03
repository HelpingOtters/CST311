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
clientName = gethostname()
serverName = gethostname() 
serverPort = 12000
BUFFER = 1024

try:

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    # sets timeout
    clientSocket.settimeout(1)
    # receives message from server
    client_status = clientSocket.recv(BUFFER)
    
    if not client_status:
        print("Did not receive message from Server:")
        clientSocket.close()

    # need validation for client ID if good then ask for message input

    sentence = input("Enter message to send to server: ")
    print(f"Message sent to server: {sentence}")

    # add code to handle awk from server. print out the awk from server

    clientSocket.send(sentence.encode())

    modifiedSentence = clientSocket.recv(BUFFER)
    print ("From Server:", modifiedSentence.decode())
except timeout:
    print("request timed out")
    clientSocket.close()


clientSocket.close()


