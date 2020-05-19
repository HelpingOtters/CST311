@@ -0,0 +1,63 @@
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

latency = [0.0] # Holds the return times

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# --- Person 1 and 2 --- #
# ADD code to...
# Send 10 pings to the server in the specified format
# Record start time
message = "Ping" #input(' ')
time_sent = 0.0
time_rcvd = 0.0
time_rtt = 0.0

for x in range(0,10):

    clientSocket.sendto(message.encode(), (serverName, serverPort))
    time_sent = time()
    #print('time_sent: ', time_sent)
    # ADD code to...
    # Get the message from the server
    # Print a “Request timed out” error or print received message
    # Record return time
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    time_rcvd = time()

    # print('time_rcvd: ', time_rcvd)
    time_rtt = (time_rcvd - time_sent)
    # print('time_rtt: ', time_rtt)
    latency.append(time_rtt)

    print(modifiedMessage.decode()) # Convert message into a string



# -----------------------------------------------------------------------------------------
# --- Person 3 and 4 --- #
# Code to determine and print out the minimum, maximum, and average RTTs
# of all pings from the client
# Print the number of packets lost and the packet loss rate (in percentage).
# Compute and print the estimated RTT, the DevRTT and the Timeout interval
# based on the RTT results.


# Close the socket to end the process
clientSocket.close()

for x in latency:
    print('latency:' '%.2E' % Decimal(x))
