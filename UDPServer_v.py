# UDP Server

# How Python makes it easy to make sockets
from socket import *
import random

# serverName here works as the IP address
# serverPort is on what port we will open up our connection
serverName = '134.10.133.158'
serverPort = 12000
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
# This gets Python to create our socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# "bind" in this case assigns the port number to our socket 
serverSocket.bind(('', serverPort))

# Set up the drop rate
dropRate = input("Percent of packets to drop (as integer): ")
assert int(dropRate) >= 0 and int(dropRate) <= 100, "Drop rate must be between 0 and 100"

# Print message just to check everything happened correctly
print("Server is ready to receive")
# Loop to be continuously listening
while True:
    # We receive, both, message and clientAddress and use 2048 buffer
    message, clientAddress = serverSocket.recvfrom(2048)
    # Modify the message as "proof" we got it at the server, note use of decode()
    modifiedMessage = message.decode().upper()
    # Send the message back, note the use of encode()
    n = random.randint(1, 100)
    if (n <= int(dropRate)):
        pass
    else:
        # Send the message back, note the use of encode()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
