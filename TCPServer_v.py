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
    # Capitalize as proof of reception
    capitalizedSentence = sentence.upper()
    # Send it back
    connectionSocket.send(capitalizedSentence.encode())
    # Close the socket
    connectionSocket.close()

'''
emily's work

while True:
    # Accept connection (UDP doesn't do this)
    connectionSocket, addr = serverSocket.accept()
    # Receive and decode
    sentence = connectionSocket.recv(1024).decode()
    req = sentence.split(' ')
    
    if req[0].upper() == "GET":
        try:
            with open(req[1], "r") as req_file:
                req_file_content = req_file.read()
                connectionSocket.send(req_file_content.encode()) #FIXME: can i do this...
    
        except FileNotFoundError:
            error_msg = "404 Not Found"
            connectionSocket.send(error_msg.encode())


    '''
    # Capitalize as proof of reception
    capitalizedSentence = sentence.upper()
    # Send it back
    connectionSocket.send(capitalizedSentence.encode())
    # Close the socket
    '''
    connectionSocket.close()
'''
