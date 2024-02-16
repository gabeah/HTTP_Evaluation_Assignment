from socket import *

# Use this port number
serverPort = 12000
# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# Bind our port number to the socket we created
serverSocket.bind(('', serverPort))
# Start listening (UDP doesn't do this)
serverSocket.listen(1)

print('Server is ready to receive')
while True:
    # Accept connection (UDP doesn't do this)
    connectionSocket, addr = serverSocket.accept()
    # Receive and decode
    sentence = connectionSocket.recv(1024).decode()
    req = sentence.split()
    
    if req[0].upper() == "GET":
        try:
            with open("." + req[1], "r", encoding = "UTF-8") as req_file:
                req_file_content = req_file.read() + "\r\n"
        
            # connectionSocket.send(req_file_content.encode()) #FIXME: can i do this...
                
            # req
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())

            # header
            connectionSocket.send("\r\n".encode())

            # content
            connectionSocket.send(req_file_content.encode())
    
        except FileNotFoundError:
            error_msg = "HTTP/1.1 404 Not Found \r\n\r\n"
            connectionSocket.send(error_msg.encode())

    else:
        error_msg = "HTTP/1.1 400 Bad Request \r\n\r\n"
        connectionSocket.send(error_msg.encode())


    '''
    # Capitalize as proof of reception
    capitalizedSentence = sentence.upper()
    # Send it back
    connectionSocket.send(capitalizedSentence.encode())
    # Close the socket
    '''
    connectionSocket.close()
