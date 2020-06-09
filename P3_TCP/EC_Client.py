"""
Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
Team: 3
Date: 06/09/2020
Title: EC_Client.py
Description: Extra Credit Assignment. This client will establish a TCP connection
to the server and wait until a second client connects with the same server. It will 
then be able to send messages back and forth to the other client, through the server.

NOTE: Must use Python 3.6.9 or greater

"""

from socket import *
from threading import *
from os import *
from signal import *

# Declare variables
serverName = 'localhost'
serverPort = 12000
messageSize = 1024
connectionOpen = False

# Function to continuously receive messages through client socket
def receiveMessage():
    global connectionOpen # Flag to indicate if the connection is open
    # Recieve messages from the server
    while True:
        message = (clientSocket.recv(1024)).decode() 
        if not message:
            break
        # If a client says bye, end the connection
        elif message.lower() == "bye":
            connectionOpen = False
            print(message)
            print("Connection closed.")
            kill(getpid(),SIGINT) # End the process
            break
        
        print(message)

# Run main routine
if __name__ == '__main__':

    # Setup client socket to server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    connectionOpen = True

    # Create thread to continuously receive messages
    receiveThread = Thread(target=receiveMessage)
    receiveThread.daemon = True
    receiveThread.start()
    
    # Loop while the client continues to send messages   
    while connectionOpen: 
        try:
            # Retrieve the clients message as input 
            message = input('')
            # Send client's message to the server
            clientSocket.send(message.encode()) 
        except KeyboardInterrupt:
            pass 
    
clientSocket.close()
