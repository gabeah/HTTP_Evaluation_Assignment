from socket import *

import time

# Use this port number
serverPort = 12000
# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# Bind our port number to the socket we created
serverSocket.bind(('', serverPort))
# Start listening (UDP doesn't do this)
serverSocket.listen(1)

print('Server is ready to receive')
'''while True:
    # Accept connection (UDP doesn't do this)
    connectionSocket, addr = serverSocket.accept()
    # Receive and decode
    sentence = connectionSocket.recv(1024).decode()
    # Capitalize as proof of reception
    capitalizedSentence = sentence.upper()
    # Send it back
    connectionSocket.send(capitalizedSentence.encode())
    # Close the socket
    connectionSocket.close()
'''
while True: # HTTP Request Handling:
    # Accept connection
    connectionSocket, addr = serverSocket.accept()

    httpRequest = connectionSocket.recv(1024).decode()
    print("Server recieved request:\r\n" + httpRequest + "at " + str(time.time()))

    splitRequest = httpRequest.split()

    if(splitRequest[0] == "GET"):
        try:
            print(splitRequest[1])
            with open(splitRequest[1], 'r') as htmlFileReq:
                print("found")
                connectionSocket.send(htmlFileReq.encode() + "\r\n")
        except FileNotFoundError:
            print("not found")
            response = "HTTP/1.1 404 Not Found\r\n\r\n"
            connectionSocket.send(response.encode())
    else:
        response = "HTTP/1.1 400 Bad Request\r\n\r\n"
        connectionSocket.send(response.encode())

    connectionSocket.close()

