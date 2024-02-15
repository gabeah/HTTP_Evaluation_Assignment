# UDP Server

# How Python makes it easy to make sockets
from socket import *

# Custom Import
import sys
import random

# serverName here works as the IP address
# serverPort is on what port we will open up our connection
# serverName = '134.10.77.129'
serverName = "127.0.0.1"
serverPort = 12000
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
# This gets Python to create our socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# "bind" in this case assigns the port number to our socket 
serverSocket.bind(('', serverPort))
# Print message just to check everything happened correctly
print ("Server is ready to receive")

#-+-+- Gabe's Work -+-+-+

# Pull drop rate (out of 100) from command-line
droprate = int(sys.argv[1])
# ensure it is a value we can work with
assert int(droprate) >= 0 and int(droprate) <= 100 
print("Drop Rate is set to " + str(droprate) + "%")

# Server Loop
while True:

    # Server waits for message on 2048 buffer
    message, clientAddress = serverSocket.recvfrom(2048)

    print("Message recieved: " + str(message))

    # Check if packet would be dropped
    if random.randrange(1, 99, 1) >= droprate:
        # Modify message, and echo back
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        print("Message sent!")
    else:
        # Report packet dropped
        print('dropped')
