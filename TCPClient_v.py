from socket import *


'''
>>>>>>> 3f1e40c (emily-work)
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
'''

serverName = input("IP Address: ")
serverPort = int(input("Port number: "))
objectPath = input("Object path: ")

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

request = "GET " + " /" + str(objectPath) + " HTTP/1.1\r\n"
clientSocket.send(request.encode())

response = clientSocket.recv(1024)
print(response.decode())

clientSocket.close()
