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

# This video talks about multithreaded servers https://www.youtube.com/watch?v=pPOBH21RnaA
# From Max: https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/
serverPort = 12000
# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET,SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    # I believe everything below this will need to be added processed in a thread.
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

   from socket import *
from threading import Thread 
from SocketServer import ThreadingMixIn 

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
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
        conn.send(message)
 
    def run(self): 
        while True:
            data = self.conn.recv(1024)
            if not data:
                # client connection closed
                break
            else:
                print "Server received data from ", clientName, data
        self.conn.close()    # close the connection and this thread is done
        
            

# Multithreaded Python server : TCP Server Socket Program Stub
SERVER_IP = '10.0.0.2' # server hostname
SERVER_PORT = 12000 
BUFFER_SIZE = 1024  # Usually 1024, but we need quick response 

serverSocket = socket(AF_INET, SOCK_STREAM)  
# tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serverSocket.bind((SERVER_IP, SERVER_PORT)) 
threads = [] 

serverSocket.listen(2)     
print ("The server is ready to receive two connections...")
clientID = 1
while True: 
    (connectionSocket, (ip,port)) = serverSocket.accept() 
    newthread = ClientThread(ip,port,connectionSocket,clientID) 
    newthread.start() 
    threads.append(newthread)
    clientID= clientID + 1
 
for t in threads: 
    t.join()  