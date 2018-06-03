import sys
from socket import socket, AF_INET, SOCK_DGRAM

serverIp = sys.argv[1]
portNumber = 5000
serverAddr = (serverIp, portNumber)
buffer = 1024

print("Client sending packets to IP {0}, via port {1}\n".format(serverIp, portNumber))

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.sendto("Connected from Ardupilot".encode('utf-8'), serverAddr)

while True:
    data = raw_input("Enter message to send or type 'exit': ")
    mySocket.sendto(myMessage1.encode('utf-8'), serverAddr)
    
    if data == "exit":
        break

sys.exit()
