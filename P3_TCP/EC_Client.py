"""
Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
Team: 3
Date: 06/09/2020
Title: EC_Client.py
Description: Extra Credit Assignment. This client will establish a TCP connection
to the server. It will then send a message to the server to be relayed to another
client. 
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
flag = Lock()
condition = Condition(flag)

# function to receive messages through client socket
def receiveMessage():
    global condition
    global connectionOpen
    try:
        
        while True:
            message = (clientSocket.recv(1024)).decode() # I moved the Decode here because it wasn't properly matching up with the elif condition - DS
            if not message:
                break
            elif message == "Connection closed":
                connectionOpen = False
                print(message)
                kill(getpid(),SIGINT) # I used this to kill the program from the OS side. The input was locking up resources. 
                                      #  Comment out this line to see what I mean. After you see "Connection closed" hit enter to end the program (without this line of code)
                break
            print(message)
           
    except error:
        print("Connection Closed")

        

        #if client wants to quit, then break loop
        # if message == 'bye':
        #     time.sleep(2)
        #     break   

        # try:
        #     message = clientSocket.recv(1024)
        #     print(message.decode())
 
        # except Exception as e:
        #     # print(e)
        #     break

# function to send messages via client socket
def sendMessage(event=None):
    try: # I added another try catch here to avoid the end of connection error
        clientSocket.send(str(message).encode('utf-8')) 
    except error:
        print("bye bye")
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
    #while connectionOpen:
    while True:
        
        message = input('')
        sendMessage()
        if not connectionOpen:
            break
        
        #if client wants to quit, then break loop
        # if message == 'bye':
        #     time.sleep(2)
        #     break   
    #close connection
    clientSocket.close()
