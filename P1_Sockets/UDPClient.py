'''
Ricardo Barbosa 
Date: May 3, 2020
Class: CST 311 
Description: The client reads a line of chatacters from its keyboard and sends the data to the server 
The client receives the modified data and displays the line on its screen

'''

# socket module
from socket import *      

# initialize variables
serverName = '127.0.0.1'    
serverPort = 12000

# create client socket; IPv4/UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# create message  to send to client 
message = raw_input('Input lowercase sentence: ')

# encode message from string type to byte type, send to its destination address
clientSocket.sendto(message.encode(), (serverName, serverPort))

# receives message and stores in variable modifiedMessage; buffer size of 2048
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()

