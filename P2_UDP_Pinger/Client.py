# Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
# Date: 05/26/20
# Title: Client.py
# Description:


from socket import *
from time import *
from decimal import Decimal

# --- Person 1 and 2 --- #
# ADD code to...
# Send 10 pings to the server in the specified format
# Record start time
# ADD code to...
# Get the message from the server
# Print a “Request timed out” error or print received message
# Record return time

# Specify socket address
serverName = 'localhost'
serverPort = 12000

time_sent = 0.0
time_rcvd = 0.0
time_rtt = 0.0
arr_rtt = [] # Holds the return times

# Creates 10 pings
for x in range(1,11):
    try:
        # Create a UDP socket
        clientSocket = socket(AF_INET, SOCK_DGRAM)  

        # Sends message to server
        message = "Ping" + str(x)
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        # Records the time when the packet was sent.
        time_sent = time()
        # Sets the timeout time for the socket. In this case 1 second.
        clientSocket.settimeout(1)
        print("Mesg sent:", message)
        
        # Receives message from server
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        # Records the time when the message comes from the server.
        time_rcvd = time()
        # Calculates RTT (latency) in ms
        time_rtt = (time_rcvd - time_sent) * 1000
        arr_rtt.append(time_rtt)

        print("Mesg rcvd:", modifiedMessage.decode())
        print("Start time:", "%.10e" % Decimal(time_sent))
        print("Return time:", "%.10e" % Decimal(time_rcvd))
        print("PONG", x, "RTT:", time_rtt, "ms\n")
        
        # Close the socket to end the process
        clientSocket.close()
    # Handles a timeout exception
    except timeout:
        print("No Mesg rcvd")
        print("PONG",x,"Request Timed out\n")
        clientSocket.close()
    
    

# -----------------------------------------------------------------------------------------
# --- Person 3 and 4 --- #
# Code to determine and print out the minimum, maximum, and average RTTs
# of all pings from the client
# Print the number of packets lost and the packet loss rate (in percentage).
# Compute and print the estimated RTT, the DevRTT and the Timeout interval
# based on the RTT results.



# for x in arr_rtt:
#     print('latency:' '%.2e' % Decimal(x))
    

