# UDP Server

# How Python makes it easy to make sockets
from socket import *

# Custom Import
import sys
import random

# serverName here works as the IP address
# serverPort is on what port we will open up our connection
serverName = '134.10.77.129.'
serverPort = 12000
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
# This gets Python to create our socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# "bind" in this case assigns the port number to our socket 
serverSocket.bind(('', serverPort))
# Print message just to check everything happened correctly
print ("Server is ready to receive")
# Loop to be continuously listening

''' Old...
while True:

    # We receive, both, message and clientAddress and use 2048 buffer
    message, clientAddress = serverSocket.recvfrom(2048)
    # Modify the message as "proof" we got it at the server, note use of decode()
    modifiedMessage = message.decode().upper()
    # Send the message back, note the use of encode()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
'''

#-+-+- Gabe's Work -+-+-+

droprate = sys.argv[1]
assert int(droprate) >= 0 and int(droprate) <= 100 

print("Drop Rate is set to " + str(droprate)) + "%")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)

    modifiedMessage = message.decode().upper()

    if random.randrange(1, 99, 1) >= droprate:
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    else:
        continue

'''
part of emily's work


dropRate = input("Percent of packets to drop (as integer): ") # FIXME: PT2


# Loop to be continuously listening
    while True:
    # We receive, both, message and clientAddress and use 2048 buffer
    message, clientAddress = serverSocket.recvfrom(2048)
    # Modify the message as "proof" we got it at the server, note use of decode()
    modifiedMessage = message.decode().upper()

    #FIXME: PT2
    n = random.randint(1, 100)
    if (n <= dropRate):
        pass
    else:
        # Send the message back, note the use of encode()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)

'''
