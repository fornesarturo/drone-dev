from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys

portNumber = 5000
buffer = 1024
hostName = gethostbyname("0.0.0.0")
serverAddr = (hostName, portNumber)

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind(serverAddr)

print("Server listening on port {0}\n".format(portNumber))

while True:
    (data, addr) = mySocket.recvfrom(buffer)
    print("Received message: " + data)
    if data == "exit":
        break

sys.exit()