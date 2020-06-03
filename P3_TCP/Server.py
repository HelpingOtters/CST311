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
    message = "test"
 
    # constructor 
    def __init__(self,ip,port,conn,clientID): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.conn = conn

        if (clientID == 1):
            print ("Accepted first connection, calling it client X")
            clientName = 'X'
            message = "Client X connected"
        else:
            print("Accepted second connection, calling it client Y")
            clientName = 'Y'
            message = "Client Y connected"
        # Sends status message back to client.

        ## this cannot be sent until server has received connection from
        # both clients
        # clients_connected = connection()
        # if clients_connected == True:
        #     conn.send(message.encode())

        
    def connection(self):
        if(len(threads) == 2):
            self.conn.send(message.encode())
        
 
## need to send message back to client with their "ID"
    
    # validates message from client
    # ***** need to rename *****
    def run(self): 
        while True:
            data = self.conn.recv(1024).decode()
            if not data:
                # client connection closed
                break
            else:
                print ("Server received data from ", clientName, data)
        self.conn.close()    # close the connection and this thread is done


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

    #if len(threads) == 2:
    #   for t in threads:
    #       t.send_message()

    # for t in threads:
    #     t.connection()

    print(f"len: {len(threads)}")
    clientID = clientID + 1
 
for t in threads: 
    t.join()  