<<<<<<< HEAD
=======
import random

>>>>>>> 3f1e40c (emily-work)
# UDP Server

# How Python makes it easy to make sockets
from socket import *

# serverName here works as the IP address
# serverPort is on what port we will open up our connection
<<<<<<< HEAD
serverName = '127.0.0.1'
=======
>>>>>>> 3f1e40c (emily-work)
serverPort = 12000
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
# This gets Python to create our socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# "bind" in this case assigns the port number to our socket 
serverSocket.bind(('', serverPort))
# Print message just to check everything happened correctly
print ("Server is ready to receive")
<<<<<<< HEAD
# Loop to be continuously listening
while True:
    # We receive, both, message and clientAddress and use 2048 buffer
    message, clientAddress = serverSocket.recvfrom(2048)
    # Modify the message as "proof" we got it at the server, note use of decode()
    modifiedMessage = message.decode().upper()
    # Send the message back, note the use of encode()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

'''
part of emily's work


dropRate = input("Percent of packets to drop (as integer): ") # FIXME: PT2
=======


dropRate = int(input("Percent of packets to drop (as integer): ")) # FIXME: PT2
>>>>>>> 3f1e40c (emily-work)


# Loop to be continuously listening
while True:
    # We receive, both, message and clientAddress and use 2048 buffer
    message, clientAddress = serverSocket.recvfrom(2048)
    # Modify the message as "proof" we got it at the server, note use of decode()
    modifiedMessage = message.decode().upper()

    #FIXME: PT2
    n = random.randint(1, 100)
<<<<<<< HEAD
    if (n <= dropRate):
=======
    if (n < dropRate):
>>>>>>> 3f1e40c (emily-work)
        pass
    else:
        # Send the message back, note the use of encode()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
<<<<<<< HEAD

'''
=======
>>>>>>> 3f1e40c (emily-work)
