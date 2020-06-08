"""
Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
Team: 3
Date: 06/09/2020
Title: EC_Client.py
Description: Extra Credit Assignment. This client will establish a TCP connection
to the server. It will then send a message to the server to be relayed to another
client. 
"""


"""
Team 1 will write the client for the regular assignment

"""
from socket import *
from threading import *
import time
from os import *
from signal import *

# variables
serverName = 'localhost'
serverPort = 12000
messageSize = 1024
encoding ='utf-8'
connectionOpen = False

# function to receive messages through client socket
def receiveMessage():
    global connectionOpen 
    try:   
        while True:
            message = (clientSocket.recv(1024)).decode() 
            if not message:
                break
            elif message == "Connection closed":
                connectionOpen = False
                print(message)
                kill(getpid(),SIGINT) 
                break
            print(message)
           
    except error:
        print("Bad Connection")
        kill(getpid(),SIGINT) 
   

# function to send messages via client socket
def sendMessage(event=None):
    try: # I added another try catch here to avoid the end of connection error - DS
        clientSocket.send(str(message).encode('utf-8')) 
    except error:
        print("Bad Connection")
        exit(1)

# run main routine
if __name__ == '__main__':

    #setup client socket to server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    connectionOpen = True

    #create thread to receive messages via function
    receiveThread = Thread(target=receiveMessage)
    receiveThread.daemon = True
    receiveThread.start()
    
    #loop keyboard input    
    while True: 
        try:
            message = input('')
            sendMessage()
        except KeyboardInterrupt:
            pass
        
        if not connectionOpen:
            break
 
    clientSocket.close()
