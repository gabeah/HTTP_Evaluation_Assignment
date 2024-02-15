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



