# UDP Client

# How Python makes it easy to make sockets
from socket import *
from socket import timeout

# =+=+=+ Added Imports =+=+=+ #
import sys
import time

# serverName here works as the IP address
# serverPort is on what port we will open up our connection
# serverName = '127.168.0.1' # Using localhost for testing on this machine
#serverName = '134.10.133.158' # Sima's Mac
serverName = '134.10.136.232' # Emily's MAC
serverPort = 12000
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
# This gets Python to create our socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Ask user for some input, lowercase just because the server will make uppercase
message = input('Input a sentence in lowercase:')

successes = 0
avg_delay = []

for i in range(10):

    sentTime = time.time()
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    clientSocket.settimeout(1) # timeout time of 5 seconds

    try:
        # Calculate delay, and append to list of all delays 
        RTT = time.time() - sentTime
        avg_delay.append(RTT)

        # recieve message, print to console
        modifiedMessage, servAddr = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode() + " recieved after " + str(RTT) + " seconds!")
        successes += 1

    except TimeoutError:
        print("Timeout occurred *** !")

# Calculate average delay
avg_rtt = 0.0
for i in avg_delay:
    avg_rtt += i

# Print to console, close the connection
print("The ping succeeded " + str(successes) + " times, with an average RTT of " + str(avg_rtt/successes) + " seconds!")
clientSocket.close()

