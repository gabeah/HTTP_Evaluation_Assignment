from socket import *

# Create socket for TCP

serverName = input("Please input destination IP: ")
serverPort = input("Please input destination port: ")
reqObj = input("Please input the path of the onject requested (without leading '/'): ")

clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect via our socket and port number to the IP
clientSocket.connect((serverName, int(serverPort)))

httpRequest = "GET /" + reqObj + " HTTP/1.1\r\n\r\n" 

# Send user input sentence
clientSocket.send(httpRequest.encode())
# Receive response from server via our socket
modifiedSentence = clientSocket.recv(1024)
# Display
print('Server response: ', modifiedSentence.decode())
clientSocket.close()
