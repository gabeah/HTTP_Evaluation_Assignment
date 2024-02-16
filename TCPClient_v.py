from socket import *

# IP address
serverName = input('Input IP address: ')
serverPort = input('Input port number: ')
objectPath = input('Input object path: ')
# Port number to use
serverPort = 12000
# Create socket for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect via our socket and port number to the IP
clientSocket.connect((serverName, serverPort))
# Ask user for a sentence to echo
request = "GET " + "/" + str(objectPath) + " HTTP/1.1\r\n"
clientSocket.send(request.encode())

# Recerve the response
response = clientSocket.recv(1024)
# Display
print('Message from server: ', response.decode())
clientSocket.close()
