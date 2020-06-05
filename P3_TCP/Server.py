# Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
# Team: 3
# Date: 06/09/2020
# Title: Server.py
# Description: This is a TCP Server program that will connect to two different
# clients simultaneously. The server will receive one message from each server 
# and will process each message. The server will then send the messages back to
# the correct client.

from socket import *
from threading import *
from time import *

# ****************** Team lets keep these links here for future reference :) ******************
# # This video talks about multithreaded servers https://www.youtube.com/watch?v=pPOBH21RnaA
# # From Max: https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/


# Define global variables
message_count = 0 # Count messages arriving at server
first_client = "" # Store name of first client to connect

# Define mutex variables 
message_count_lock = Lock() # Lock for the message_count variable
message_cv = Condition(message_count_lock) # A CV to wait for server to receive both messages 


# Creates a class for each client thread
class ClientThread(Thread):  
    # Constructor 
    def __init__(self, ip, port, connection, client_id): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.connection = connection
        self.client_name = ""
        self.ack_message = ""
        self.timestamp = 0.0
        # Assigns client names to thread and sets ack_message message
        if (client_id == 1):
            print ("Accepted first connection, calling it client X")
            self.client_name = "X"
            self.ack_message = "Client X connected"
        else:
            print("Accepted second connection, calling it client Y")
            self.client_name = "Y"
            self.ack_message = "Client Y connected"

    def run(self):
        global message_count 
        global first_client
        self.server_output = ""
        self.client_message = ""
        while True:
            self.client_message = self.connection.recv(1024).decode()
            if not self.client_message:
                # client connection closed
                break
            else:
                message_cv.acquire()  # acquire the lock to update message counter
                
                # If this is the first message
                if (message_count == 0):
                    self.server_output = f"Client {self.client_name}: {self.client_message}" 
                    message_count = message_count + 1 
                    # store client_id of the client that returned the first message
                    first_client = self.client_name
                
                # If this is the second message
                else:
                    self.server_output = f"Client {self.client_name}: {self.client_message}" 
                    message_count = message_count + 1

                print("Client ", self.client_name, " sent message ", message_count, ": ", self.client_message)
                
                message_cv.notify()   # to notify the main thread a message is received
                message_cv.release()  # release the lock
               
        self.connection.close()    # close the connection and this thread is done

    # *************** Note for Team 2, OK to delete this comment. You can probably use this for the EC? ******************
    # If not, then delete this method.
    # Returns the thread's connetion socket
    def get_connection(self):
        return self.connection
    # Returns the acknowledgment message
    def get_ack_message(self):
        return self.ack_message
    # Returns the client's name
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

    print("Waiting a bit for clients to close connections")

    for t in threads: 
        t.join()

    print("Done.")

if __name__ == "__main__":
    main()