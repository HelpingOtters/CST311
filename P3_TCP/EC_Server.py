"""
Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
Team: 3
Date: 06/09/2020
Title: EC_Server.py
Description: Extra Credit Assignment. This server will act as the processing 
relay between two clients. It will receive two connections from two different 
clients. Each client will then send a message to the other client via the 
server.

NOTE: Must use Python 3.6.9 or greater

"""

from socket import *
from threading import *

# ****************** Team, lets keep these links here for future reference :) ******************
# # This video talks about multithreaded servers https://www.youtube.com/watch?v=pPOBH21RnaA
# # From Max: https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/

# Define global variable to hold both connections
connections = []

# Creates a class for each client connection
class ClientConnection(Thread):  
    # Constructor 
    def __init__(self, ip, port, connection, client_id): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.connection = connection
        self.ack_message = "\nBoth clients have connected. Begin chatting."
        # Sets ack_message based on when this client connected
        if (client_id == 1):
            print ("Accepted first connection.")
        else:
            print("Accepted second connection.")

    # Returns the acknowledgment message
    def get_ack_message(self):
        return self.ack_message

    # Sends the client an acknowledgment message, establishing the connection 
    def send_ack_message(self):
        try:     
            self.connection.send(self.get_ack_message().encode())
        except error:
            print("Bad Connection")
            exit(1)

    # Sends a message to the client
    def send_message(self,message):
        self.connection.send(message.encode())

    # Method that runs when start() is called on a ClientConnection object
    # This method recieves messages from one client and sends them to the 
    # other client.
    def run(self):
        self.client_message = ""
        # Continuously check for incoming messages 
        while True:
            self.client_message = self.connection.recv(1024).decode()

            if not self.client_message:
                break
            
            # If a client says "bye", close the connection
            if self.client_message.lower() == "bye":
                for thread in connections:
                    thread.send_message(self.client_message)
                break
                
            # Send the incoming message to the receiveing client, but not 
            # the sending client
            for thread in connections:
                if thread.connection != self.connection:
                    thread.send_message(self.client_message)
                
        self.connection.close() # end this connection 

# --------------------------------------- End of Class --------------------------------------- #

# Main method
def main():
    # Multithreaded Python server : TCP Server Socket Program Stub
    SERVER_PORT = 12000 
    BUFFER_SIZE = 1024  # Usually 1024, but we need quick response 

    serverSocket = socket(AF_INET, SOCK_STREAM)  
    serverSocket.bind(('', SERVER_PORT)) 
    # Holds the connection threads
    global connections

    # Use 2 as a parameter, to allow for 2 connections
    serverSocket.listen(2)      
    print ("The server is ready to receive two connections...\n")
    client_id = 1 # Used to identify the client

    # Accept arriving connections
    while True: 
        (connectionSocket, (ip,port)) = serverSocket.accept() 
        # Create a new client connection
        new_connection = ClientConnection(ip,port,connectionSocket,client_id) 
        new_connection.daemon = True
        new_connection.start() 
        # Add the new connection to the connections array
        connections.append(new_connection)
        client_id = client_id + 1

        # Check that there are two clients before finalizing the connection
        if(len(connections) == 2):
            for c in connections:
                c.send_ack_message()
            break

    print("\nClients are chatting")

    # Wait for both client connection threads to complete
    for c in connections: 
        c.join()

    print("Both connections closed.")

# ------------------------------- Run Main ---------------------------------- #
if __name__ == "__main__":
    main()
