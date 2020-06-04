# Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
# Team: 3
# Date: 06/09/2020
# Title: Server.py
# Description: This is a TCP Server program will will connect to two different
# clients simultaneously. The server will receive one message from each server 
# and will process each message. The server will then send the messages back to
# the correct client.

from socket import *
from threading import *
from time import *

# ****************** Team lets keep these links here for future reference :) ******************
# # This video talks about multithreaded servers https://www.youtube.com/watch?v=pPOBH21RnaA
# # From Max: https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/


# Counter for counting messages arrived to server
msgCtr = 0
# Message to be sent to all clients
msg = ""
# A lock to protect the msgCtr update
msgCtr_lock = Lock()
# A condition variable to wait for message received by both client threads
cvToSend = Condition(msgCtr_lock)
# Stores the client name of the client that connected first
first_client = ""

# Creates a class for each client thread
class ClientThread(Thread):  
    # constructor 
    def __init__(self,ip,port,conn,clientID): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.conn = conn
        self.clientName = ""
        self.handshake = ""
        self.timestamp = 0.0
        # Assigns client names to thread and sets handshake message
        if (clientID == 1):
            print ("Accepted first connection, calling it client X")
            self.clientName = "X"
            self.handshake = "Client X connected"
        else:
            print("Accepted second connection, calling it client Y")
            self.clientName = "Y"
            self.handshake = "Client Y connected"

    def run(self):
        global msgCtr 
        self.server_output = ""
        self.client_message = ""
        while True:
            self.client_message = self.conn.recv(1024).decode()
            if not self.client_message:
                # client connection closed
                break
            else:
                cvToSend.acquire()  # acquire the lock to update message counter
                
                 # it is the first message
                if (msgCtr == 0):

                    # ****************** Note for Max: Flagged for deletion *****************
                    #self.server_output = self.clientName + ": " + self.client_message + " received before "
                    self.server_output = f"Client {self.clientName}: {self.client_message}" 
                    msgCtr = msgCtr + 1 
                    # store clientID of the client that returned the first message
                    first_client = self.clientName
                
                # it is the second message
                else:

                    # ************** Note for Max: Do you think we should use these to generate the message that is broadcast to all clients? ************
                    ## ************* Max, delete this (below) if you don't agree with my idea that i sent yo on slack ********************************************
                    self.server_output = f"Client {self.clientName}: {self.client_message}" 
                    #self.server_output = self.server_output + self.clientName + ": " + self.client_message

                    msgCtr = msgCtr + 1
                print("Client ", self.clientName, " sent message ", msgCtr, ": ", self.client_message)
                
                cvToSend.notify()   # to notify the main thread a message is received
                cvToSend.release()  # release the lock
               
        self.conn.close()    # close the connection and this thread is done

    # *************** Note for Team 2, OK to delete this comment. You can probably use this for the EC? ******************
    # If not, then delete this method.
    # Returns the thread's connetion socket
    def get_connections(self):
        return self.conn
    # Returns the handshake message
    def get_handshake(self):
        return self.handshake
    # Returns the client's name
    def get_client_name(self):
        return self.clientName
    # Sends clients a handshake messaging allowing client to send message back
    def send_handshake(self):
        self.conn.send(self.get_handshake().encode())

    # ************************************* Max delete this if you don't agree with my idea from slack *****************************************
    def get_server_output(self):
        return self.server_output
    #Sends a message to client
    def send_message(self,message):
        self.conn.send(message.encode())

# Multithreaded Python server : TCP Server Socket Program Stub
SERVER_PORT = 12000 
BUFFER_SIZE = 1024  # Usually 1024, but we need quick response 

serverSocket = socket(AF_INET, SOCK_STREAM)  
serverSocket.bind(('', SERVER_PORT)) 
threads = []

# using 2 as a parameter to allow for 2 connections to be queued
serverSocket.listen(2)      
print ("The server is ready to receive two connections...")
clientID = 1 # used to identify the client

while True: 
    (connectionSocket, (ip,port)) = serverSocket.accept() 
    newthread = ClientThread(ip,port,connectionSocket,clientID) 
    newthread.start() 
    threads.append(newthread)
    clientID = clientID + 1
    
    # Checks for even number of clients before sending handshake messages to clients.
    if(len(threads) % 2 == 0):
        for t in threads:
            t.send_handshake()
        break

# wait for both threads to receive a message
cvToSend.acquire()
while (msgCtr != 2):
    cvToSend.wait() # wait for a thread's notification for any message received

# message is ready to send to all the clients
if first_client == "X":
    #constructs broadcast message
    print(f"**************Tracer: thread 0: {threads[0].clientName} thread 1: {threads[1].clientName}") # tracer
    broadcast_message = f"{threads[0].get_server_output()} before {threads[1].get_server_output()}"
    print(f"***********Tracer after message is made! {broadcast_message}*************")

    # sends broadcast message to all clients
    for t in threads:
        print(f"***********Tracer inside for loop! {broadcast_message}*************")

        t.send_message(broadcast_message)
else:
    print(f"**************Tracer: thread 0: {threads[0].clientName} thread 1: {threads[1].clientName}") # tracer
    broadcast_message = f"{threads[1].get_server_output()} before {threads[0].get_server_output()}"
    print(f"***********Tracer after message is made! {broadcast_message}*************")
    for t in threads:
        print(f"***********Tracer inside for loop! {broadcast_message}*************")

        t.send_message(broadcast_message)

print("Waiting a bit for clients to close connections")

for t in threads: 
    t.join()
print("Done.")