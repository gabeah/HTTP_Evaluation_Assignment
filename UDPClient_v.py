# UDP Client

# How Python makes it easy to make sockets
from socket import *

# =+=+=+ Added Imports =+=+=+ #
import sys

# serverName here works as the IP address
# serverPort is on what port we will open up our connection
#serverName = '127.168.0.1' Using localhost for testing on this machine
serverName = '134.10.133.158'
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

# emily's thoughts for q3
'''
# serverName here works as the IP address
# serverPort is on what port we will open up our connection
serverName = '127.168.0.1'
serverPort = 12000

# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
# This gets Python to create our socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# FIXME: PT3
for i in range(10): 
    p = "ping"

    avgDelay = []
    receivedCount = 0

    sentAt = time.time()
    clientSocket.sendto(p.encode(), (serverName, serverPort))

    clientSocket.settimeout(5) # 5 seconds or less
    timeOut = True

    while not socket.timeout:
        try:
            response = clientSocket.recvfrom(2048)
            receivedAt = time.time()
            timeOut = False
            receivedCount += 1

            print(response.decode())
            
            RTT = receivedAt - sentAt
            avgDelay.append(RTT)
            print("RTT: " + str(RTT))
        except Exception as e:
            pass
    
    if timeOut:
        print("*")

#avg delay
sum = 0

for RTT in avgDelay:
    sum += RTT

sum /= len(avgDelay)
print("Average delay: " + str(sum))

#packet loss rate
print("Packet loss rate: " + str(receivedCount/10))

clientSocket.close()
'''
