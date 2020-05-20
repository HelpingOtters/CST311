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
# Print a "Request timed out" error or print received message
# Record return time

# Specify socket address
serverName = 'localhost'
serverPort = 12000

#message = "Ping" 
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
        time_sent = time()
        clientSocket.settimeout(1)
        print("Mesg sent:", message)
        
        # Receives message from server
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        time_rcvd = time()
        
        print("Mesg rcvd:", modifiedMessage.decode())
        print("Start time:" "%.10E" % Decimal(time_sent))
        print("Return time:", "%.10E" % Decimal(time_rcvd))
        # Calculates RTT (latency).
        time_rtt = (time_rcvd - time_sent)
        print("PONG", x, "RTT:", "%.10E" % Decimal(time_rtt), "ms\n")
        arr_rtt.append(time_rtt)
        # Close the socket to end the process
        clientSocket.close()

    except timeout :
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


# Find and print the minimum and maximum from the arr_rtt[] and pacet loss rate
min_rtt = min(arr_rtt)
max_rtt = max(arr_rtt)
avg_rtt = 0 if len(arr_rtt) == 0 else sum(arr_rtt)/len(arr_rtt)
packet_loss_rate = (10.0 - len(arr_rtt)) / 10;

print("Min RTT:\t", min_rtt, " ms");
print("Max RTT:\t", max_rtt, " ms");
print("Average RTT:\t", avg_rtt, " ms" );
print("Packet Loss:\t", packet_loss_rate);
    


# for x in arr_rtt:
#     print('latency:' '%.2E' % Decimal(x))
    

