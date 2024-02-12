from socket import *

# IP address
serverName = '134.10.122.184'
# Port number to use
serverPort = 12000
# Create socket for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect via our socket and port number to the IP
clientSocket.connect((serverName, serverPort))
# Ask user for a sentence to echo
sentence = input('Input a sentence in lowercase:')
# Send user input sentence
clientSocket.send(sentence.encode())
# Receive response from server via our socket
modifiedSentence = clientSocket.recv(1024)
# Display
print('Message from server: ', modifiedSentence.decode())
clientSocket.close()
