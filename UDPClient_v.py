# UDP Client

# How Python makes it easy to make sockets
from socket import *

# serverName here works as the IP address
# serverPort is on what port we will open up our connection
serverName = '127.168.0.1'
serverPort = 12000
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
# This gets Python to create our socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Ask user for some input, lowercase just because the server will make uppercase
message = input('Input a sentence in lowercase:')
# Use socket to send message, note the use of encode() and the address
clientSocket.sendto(message.encode(), (serverName, serverPort))
# Receiving follows similar format, 2048 is buffer size for input
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()



