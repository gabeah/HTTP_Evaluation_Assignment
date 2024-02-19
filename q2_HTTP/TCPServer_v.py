from socket import *

import time

# Use this port number
# serverName = '134.10.77.129'
# serverPort = 12000
serverPort = 43285
# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind our port number to the socket we created
serverSocket.bind(('', serverPort))
print(serverSocket.getsockname())
# Start listening (UDP doesn't do this)
serverSocket.listen(1)

print('Server is ready to receive')

while True: # HTTP Request Handling:
    # Accept connection
    connectionSocket, addr = serverSocket.accept()

    # Decode, and print request to console
    httpRequest = connectionSocket.recv(1024).decode()
    print("Server recieved request:\r\n" + httpRequest + "at " + str(time.time()))

    # Break into parsable segments
    splitRequest = httpRequest.split()

    if(splitRequest[0].upper() == "GET"):
        # attempt to find /
        try:
            print(splitRequest[1]) # printing for debugging
            
            # open request file, encode/read in UTF-8
            with open("."+splitRequest[1], 'r', encoding = "UTF-8") as htmlFileReq:
                print("found") # printing for debugging
                response = htmlFileReq.read() + "\r\n"
            
            # Send response (with debug prints)
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            print("status sent")
            connectionSocket.send("Content-Type: text/html; charset=UTF-8\r\n".encode())
            print("header sent")
            connectionSocket.send("\r\n".encode())
            print("blank sent")
            connectionSocket.send(response.encode())

        except FileNotFoundError:
            print("not found")
            response = "HTTP/1.1 404 Not Found\r\n\r\n"
            connectionSocket.send(response.encode())
    else:
        response = "HTTP/1.1 400 Bad Request\r\n\r\n"
        connectionSocket.send(response.encode())
    print("request done")
    connectionSocket.close()

