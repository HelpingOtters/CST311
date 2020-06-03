# Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
# Team: 3
# Date: 06/09/2020
# Title: Server.py
# Description: This is a TCP Server program will will connect to two different
# clients simultaneously. The server will receive one message from each server 
# and will process each message. The server will then send the messages back to
# the correct client.

from socket import *
from threading import Thread
from time import *

# # This video talks about multithreaded servers https://www.youtube.com/watch?v=pPOBH21RnaA
# # From Max: https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/


# Multithreaded Python server : TCP Server Socket Thread Pool
clientName = ""
#xCtr = 0
#yCtr = 0



# sends the order awk to the clients    
#def awk():

 #   if: ()
  #      return awk1
  #  else:
   #     return awk2   



class ClientThread(Thread): 

 
    # constructor 
    def __init__(self,ip,port,conn,clientID): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.conn = conn
        self.clientName = ""
        self.greeting = ""
        self.message = ""
        self.timestamp = 0.0
        if (clientID == 1):
            print ("Accepted first connection, calling it client X")
            self.clientName = 'X'
            self.greeting = "Client X connected"
        else:
            print("Accepted second connection, calling it client Y")
            self.clientName = 'Y'
            self.greeting = "Client Y connected"
    
    def get_greeting(self):
        return self.greeting
    
    def get_client_name(self):
        return self.clientName
    
    def send_message(self):
        self.conn.send(self.get_greeting().encode())

    def get_message(self):
        return self.message

    def set_time(self):
       self.timestamp = time()

    def get_time(self):
        return self.timestamp

    def receive_message(self):
        self.message = self.conn.recv(1024).decode()
        if self.message:
            self.set_time()
            print(f"Message from {self.clientName}: {self.message}")
    
   

    def send_awk(self):
        test = ""
    
       


#awk1 = "X: received before Y"
#awk2 = "Y: received before X"



# Multithreaded Python server : TCP Server Socket Program Stub
SERVER_IP = gethostname() # server hostname 
SERVER_PORT = 12000 
BUFFER_SIZE = 1024  # Usually 1024, but we need quick response 

serverSocket = socket(AF_INET, SOCK_STREAM)  
# tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serverSocket.bind((SERVER_IP, SERVER_PORT)) 
threads = [] 

# using 2 as a parameter to allow for 2 connections to be queued
serverSocket.listen(2)     
print ("The server is ready to receive two connections...")
clientID = 1
while True: 
    (connectionSocket, (ip,port)) = serverSocket.accept() 
    newthread = ClientThread(ip,port,connectionSocket,clientID) 
    newthread.start() 
    threads.append(newthread)

    # sends messages back to clients after two connections
    if (len(threads) % 2 == 0):
        for t in threads:
            t.send_message()
        for t in threads:
            t.receive_message()
        if threads[0].get_time() < threads[1].get_time():
            print(f"Thread 0 time: {threads[0].get_time()} Thread 1 time: {threads[1].get_time()}")
            print("client x first")
            print(f"Client {threads[0].get_client_name()}: {threads[0].get_message()}")
            print(f"Client {threads[1].get_client_name()}: {threads[1].get_message()}")
        else:
            print(f"Thread 0 time: {threads[0].get_time()} Thread 1 time: {threads[1].get_time()}")
            print("client y first")
            print(f"Client {threads[1].get_client_name()}: {threads[1].get_message()}")
            print(f"Client {threads[0].get_client_name()}: {threads[0].get_message()}")

                
    # print(f"len: {len(threads)}") # tracer
    clientID = clientID + 1
 
for t in threads: 
    t.join()  