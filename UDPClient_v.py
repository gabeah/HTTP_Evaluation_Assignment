# UDP Client

# How Python makes it easy to make sockets
from socket import *
import time

# serverName here works as the IP address
# serverPort is on what port we will open up our connection
# serverName = '127.0.0.1' # Using localhost for testing on this machine
# serverName = '134.10.77.129' # gabe
serverName = '134.10.136.232' # emily
serverPort = 12000
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
# This gets Python to create our socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

rtts = []

for i in range(10):
    MESSAGE = "ping"
    clientSocket.settimeout(5)
    # Use socket to send message, note the use of encode() and the address
    clientSocket.sendto(MESSAGE.encode(), (serverName, serverPort))
    # Start the timer
    sent_at = time.time()

    try:
        # Receiving follows similar format, 2048 is buffer size for input
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        # Stop the timer
        received_at = time.time()
        print(modifiedMessage.decode())
        RTT = received_at - sent_at
        rtts.append(RTT)
        print("RTT (ms): " + str(RTT * 1000))
    except TimeoutError:
        print("*")

avg_delay = sum(rtts) / len(rtts)
print("Average delay (ms): " + str(avg_delay  * 1000))

packet_loss_rate = 1 - (len(rtts) / 10)
print("Packet loss rate: " + str(packet_loss_rate))

clientSocket.close()

# 1c 50 % rate
# PING
# RTT (ms): 57.541847229003906
# *
# *
# PING
# RTT (ms): 10.744810104370117
# PING
# RTT (ms): 7.340192794799805
# *
# PING
# RTT (ms): 8.53586196899414
# PING
# RTT (ms): 7.549047470092773
# *
# *
# Average delay (ms): 18.34235191345215
# Packet loss rate: 0.5

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
