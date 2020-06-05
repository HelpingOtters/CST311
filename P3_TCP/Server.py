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
        self.connection = connection
        self.client_name = ""
        self.ack_message = ""
        self.timestamp = 0.0 # I think this is ok to delete ***********************
        # Assigns client names to thread and sets ack_message message
        if (client_id == 1):
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
        return self.client_name
    # Sends clients an acknowledgment message, allowing client to send message back
    def send_ack_message(self):
        self.connection.send(self.get_ack_message().encode())
    def get_server_output(self):
        return self.server_output
    #Sends a message to client
    def send_message(self,message):
        self.connection.send(message.encode())

# Broadcasts the order awk message to all clients
def send_order_awk(threads,first_client):
        # message is ready to send to all the clients
    if first_client == "X":
        #constructs broadcast message
        broadcast_message = f"{threads[0].get_server_output()} before {threads[1].get_server_output()}"

        # sends broadcast message to all clients
        for t in threads:
            t.send_message(broadcast_message)
    else:
        broadcast_message = f"{threads[1].get_server_output()} before {threads[0].get_server_output()}"

        for t in threads:
            t.send_message(broadcast_message)

def main():
    # Multithreaded Python server : TCP Server Socket Program Stub
    SERVER_PORT = 12000 
    BUFFER_SIZE = 1024  # Usually 1024, but we need quick response 

    serverSocket = socket(AF_INET, SOCK_STREAM)  
    serverSocket.bind(('', SERVER_PORT)) 
    threads = []

    # using 2 as a parameter to allow for 2 connections to be queued
    serverSocket.listen(2)      
    print ("The server is ready to receive two connections...")
    client_id = 1 # used to identify the client

    while True: 
        (connectionSocket, (ip,port)) = serverSocket.accept() 
        newthread = ClientThread(ip,port,connectionSocket,client_id) 
        newthread.start() 
        threads.append(newthread)
        client_id = client_id + 1

        # Checks that there is more than one client before finalizing the connection
        if(len(threads) > 1):
            for t in threads:
                t.send_ack_message()
            break

    # wait for both threads to receive a message
    message_cv.acquire()
    while (message_count != 2):
        message_cv.wait() # wait for a thread's notification for any message received

    send_order_awk(threads,first_client)

    ## TESTED METHOD OK TO DELETE THIS block
    # # message is ready to send to all the clients
    # if first_client == "X":
    #     #constructs broadcast message
    #     broadcast_message = f"{threads[0].get_server_output()} before {threads[1].get_server_output()}"

    #     # sends broadcast message to all clients
    #     for t in threads:
    #         t.send_message(broadcast_message)
    # else:
    #     broadcast_message = f"{threads[1].get_server_output()} before {threads[0].get_server_output()}"

    #     for t in threads:
    #         t.send_message(broadcast_message)

    print("Waiting a bit for clients to close connections")

    for t in threads: 
        t.join()

    print("Done.")

# Runs Main Method -------------------------------------------------------------
if __name__ == "__main__":
    main()
