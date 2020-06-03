# Names: Ricardo Barbosa, Max Halbert, Lindsey Reynolds and Dan Sedano
# Team: 3
# Date: 05/26/20
# Title: Client.py
# Description: This program sends 10 pings to the server program, 
# keeping track of the RTTs of each ping. It tracks the number of 
# lost packets and calculates the min, max and average RTTs. It also
# calculates estimatedRTT, devRTT and timeout interval for the sequence.

from socket import *
from time import *
from decimal import Decimal

# Specify socket address
serverName = '68.7.168.214'
serverPort = 12000

time_sent = 0.0
time_rcvd = 0.0
time_rtt = 0.0
# --- Person 1 and 2 --- #
# ADD code to...
# Send 10 pings to the server in the specified format
# Record start time
# ADD code to...
# Get the message from the server
# Print a “Request timed out” error or print received message
# Record return time
# Sets the socket timeout timer
# Creates 10 Pings

sum_rtt = 0.0   # total sum of RTT of returned pings
num_pongs = 0   # number of returned pings
min_rtt = 1000.0   # set the minimum of RTT to the maximum timout in milliseconds
max_rtt = 0.0   # set the maximum of RTT to 0

# Declare values for calculating estimatedRTT and devRTT
a = .125
B = .25
estimatedRTT = 0
devRTT = 0

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

        # Sets the timeout time for the socket to 1 second
        clientSocket.settimeout(1)
        
        # Receives message from server
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        # Records the time when the message comes from the server
        time_rcvd = time()
        # Calculates RTT (latency) in ms
        time_rtt = (time_rcvd - time_sent) * 1000
        
        # Sum up the RTT of returned message, and update min and max of RTT
        sum_rtt = sum_rtt + time_rtt
        if (min_rtt > time_rtt):
            min_rtt = time_rtt
        if (max_rtt < time_rtt):
            max_rtt = time_rtt
		# Increment the counter of pongs
        num_pongs = num_pongs + 1    

        # Calculate estimated RTT and dev RTT
        if(x == 1): # If this is the first sample
            estimatedRTT = time_rtt 
            devRTT = estimatedRTT/2
        else: 
            # Use formulas to calculate estimatedRTT and devRTT
            estimatedRTT = ((1 - a) * estimatedRTT) + (a * time_rtt)
            devRTT = ((1 - B) * devRTT) + (B * abs(time_rtt - estimatedRTT))

        print("Mesg sent:", message)
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

# Calculate the average RTT time
avg_rtt = sum_rtt / num_pongs

# Calculate the percentage of lost packets
packet_loss_rate = (10.0 - num_pongs) * 100 / 10

# Get the timeout interval value
timeout = estimatedRTT + (4 * devRTT)

print("Min RTT:\t\t", min_rtt, " ms")
print("Max RTT:\t\t", max_rtt, " ms")
print("Average RTT:\t\t", avg_rtt, " ms" )
print("Packet Loss:\t\t", packet_loss_rate, "%")
print("Estimated RTT:\t\t", estimatedRTT, " ms")
print("Dev RTT:\t\t", devRTT, " ms")
print("Timeout Interval:\t", timeout, " ms")
