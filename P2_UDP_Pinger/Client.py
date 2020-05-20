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

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = "Ping" 
time_sent = 0.0
time_rcvd = 0.0
time_rtt = 0.0
arr_rtt = [] # Holds the return times

# Creates 10 pings
for x in range(0,10):
    try:
        # Sends message to server
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        time_sent = time()
        clientSocket.settimeout(1)

        # Receives message from server
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        time_rcvd = time()

        # Calculates RTT (latency).
        time_rtt = (time_rcvd - time_sent)
        print("PONG ", x, " RTT: ", "%.10E" % Decimal(time_rtt))
        arr_rtt.append(time_rtt)

        print(modifiedMessage.decode()) # Convert message into a string

    except timeout :
        print("Request timed out")
        clientSocket.close()
    
    # Close the socket to end the process
    clientSocket.close()

# -----------------------------------------------------------------------------------------
# --- Person 3 and 4 --- #
# Code to determine and print out the minimum, maximum, and average RTTs
# of all pings from the client
# Print the number of packets lost and the packet loss rate (in percentage).
# Compute and print the estimated RTT, the DevRTT and the Timeout interval
# based on the RTT results.



for x in arr_rtt:
    print('latency:' '%.2E' % Decimal(x))
    

