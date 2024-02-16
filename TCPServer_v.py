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
while True: # HTTP Request Handling:
    # Accept connection
    connectionSocket, addr = serverSocket.accept()

    # Decode, and print request to console
    httpRequest = connectionSocket.recv(1024).decode()
    print("Server recieved request:\r\n" + httpRequest + "at " + str(time.time()))

    #     Server recieved request:
    # GET /favicon.ico HTTP/1.1
    # Host: 134.10.133.158:12000
    # Connection: keep-alive
    # User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36
    # Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
    # Referer: http://134.10.133.158:12000/index.html
    # Accept-Encoding: gzip, deflate
    # Accept-Language: en-US,en;q=0.9

    # Break into parsable segments
    splitRequest = httpRequest.split()

    if (splitRequest[0].upper() == "GET"):
        try:
            print(splitRequest[1]) # printing for debugging
            with open(splitRequest[1][1:], 'r', encoding="UTF-8") as htmlFileReq:
                print("found") # printing for debugging
                response = htmlFileReq.read() + "\r\n"

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
