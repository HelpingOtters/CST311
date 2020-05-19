
# Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
# Date: 05/26/20
# Title: Client.py
# Description:


from socket import *
from time import *
from decimal import Decimal

# Specify socket address
serverName = 'localhost'
serverPort = 12000

latency = [] # Holds the return times



# --- Person 1 and 2 --- #
# ADD code to...
# Send 10 pings to the server in the specified format
# Record start time
message = "Ping" #input(' ')
time_sent = 0.0
time_rcvd = 0.0
time_rtt = 0.0

# Creates 10 Pings
for x in range(0,10):

    try:
        # Create a UDP socket
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        time_sent = time()
        #print('time_sent: ', time_sent)
        # ADD code to...
        # Get the message from the server
        # Print a “Request timed out” error or print received message
        # Record return time
        # Sets the socket timeout timer
        clientSocket.settimeout(1.0)
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        time_rcvd = time()

        # Calculates the RTT (latency)
        time_rtt = (time_rcvd - time_sent)
        # Adds latency to List
        latency.append(time_rtt)
        print(modifiedMessage.decode()) # Convert message into a string
        # Close the socket to end the process
        clientSocket.close()
    # Catches the timeout exception    
    except timeout:
        print('Request timed out')
        clientSocket.close()
 
   



# -----------------------------------------------------------------------------------------
# --- Person 3 and 4 --- #
# Code to determine and print out the minimum, maximum, and average RTTs
# of all pings from the client
# Print the number of packets lost and the packet loss rate (in percentage).
# Compute and print the estimated RTT, the DevRTT and the Timeout interval
# based on the RTT results.



for x in latency:
    print(x , 'latency: '  '%.2E' % Decimal(x))
