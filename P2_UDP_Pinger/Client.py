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

time_sent = 0.0
time_rcvd = 0.0
time_rtt = 0.0
arr_rtt = [] # Holds the return times

sum_rtt = 0.0   # total sum of RTT of returned pings
num_pongs = 0   # number of returned pings
min_rtt = 1000.0   # set the minimum of RTT to the maximum timout in milliseconds
max_rtt = 0.0   # set the maximum of RTT to 0

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
        
        # sum up the RTT of returned message, and update min and max of RTT
        sum_rtt = sum_rtt + time_rtt
        if (min_rtt > time_rtt):
            min_rtt = time_rtt
        if (max_rtt < time_rtt):
            max_rtt = time_rtt
		# increment the counter of pongs
        num_pongs = num_pongs + 1    
        

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


# Find and print the minimum and maximum from the arr_rtt[] and pacet loss rate
#min_rtt = min(arr_rtt)
#max_rtt = max(arr_rtt)
#avg_rtt = 0 if len(arr_rtt) == 0 else sum(arr_rtt)/len(arr_rtt)
#packet_loss_rate = (10.0 - len(arr_rtt)) * 100 / 10

avg_rtt = sum_rtt / num_pongs
packet_loss_rate = (10.0 - num_pongs) * 100 / 10

print("Min RTT:\t", min_rtt, " ms");
print("Max RTT:\t", max_rtt, " ms");
print("Average RTT:\t", avg_rtt, " ms" );
print("Packet Loss:\t", packet_loss_rate, "%");

a = .125
B = .25

estimatedRTT = arr_rtt[0]
devRTT = estimatedRTT/2

print("For 1 EstimatedRTT: ", estimatedRTT)
    print("DevRTT: ", devRTT)

# Get the Estimated RTT and Dev RTT
for i in range(1, len(arr_rtt)):
    estimatedRTT = ((1 - a) * estimatedRTT) + (a * arr_rtt[i])
    devRTT = ((1 - B) * devRTT) + (B * abs(arr_rtt[i] - estimatedRTT))
    ping = i + 1
    print("For ", ping, "EstimatedRTT: ", estimatedRTT)
    print("DevRTT: ", devRTT)

# Get the timeout interval value
timeout = estimatedRTT + (4 * devRTT)

print("\n\nEstimated RTT:\t", estimatedRTT, " ms")
print("Dev RTT:\t", devRTT, " ms")
print("Timeout Interval: ", timeout, " ms")

    
# for x in arr_rtt:
#     print('latency:' '%.2e' % Decimal(x))
    

