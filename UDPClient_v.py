# UDP Client

# How Python makes it easy to make sockets
from socket import *

# =+=+=+ Added Imports =+=+=+ #
import sys
import time

# serverName here works as the IP address
# serverPort is on what port we will open up our connection
serverName = '127.168.0.1' # Using localhost for testing on this machine
#serverName = '134.10.133.158'
serverPort = 12000
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
# This gets Python to create our socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Ask user for some input, lowercase just because the server will make uppercase
message = input('Input a sentence in lowercase:')

successes = 0
avg_delay = []

for i in range(10):

    msg = "ping"

    sentTime = time.time()
    clientSocket.sendto(msg.encode(), (serverName, serverPort))

    clientSocket.settimeout(5) # timeout time of 5 seconds

    try: 
        modifiedMessage, servAddr = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())
    except socket.timeout:
        print("Timeout occurred")






clientSocket.close()

