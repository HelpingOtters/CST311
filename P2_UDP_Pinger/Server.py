# Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
# Team: 3
# Date: 05/26/20
# Title: Server.py
# Description: This file emulates a UDP server with approximately 
# 30% packet loss rate

import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

# Keeps track of the successful pings
numPings = 0

print("Waiting for Client....\n")
while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        print("Packet was lost.\n")
        continue

    # Otherwise, the server responds
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), address)

    numPings = numPings + 1


    # Print specified text to the console
    print("PING", numPings, "Received")
    print("Mesg rcvd: ", message.decode())
    print("Mesg sent: ", modifiedMessage, "\n")
