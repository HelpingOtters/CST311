"""
    Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
    Team: 3
    Date: 06/09/2020
    Title: Client.py
    Description: This is the client program which will be connected to a server 
    using a TCP connection. This program will send a message to the server then
    will receive a response from the server. 


NOTE: To Run Please use Python3 command. This program was written and tested with Python 3.6.9 and higher.

"""

from socket import *
# In your command prompt, type in hostname and press enter.
# What comes up is your computer's hostname
serverName = gethostname() # since it's running on one machine
serverPort = 12000
BUFFER = 1024

# Try block for connection
try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

except error:
    print("Unable to connect")
    exit(1)

# receives message from server
print("Waiting for other client...")

# Receives handshake message from server.
# ClientSocket will not execute until message is received
connection_status = clientSocket.recv(BUFFER)

print(connection_status.decode())
sentence = input("Enter message to send to server: ")
clientSocket.send(sentence.encode())
# Accepts awk message from server 
awk_message = clientSocket.recv(BUFFER)
print (awk_message.decode())

clientSocket.close()  
    
