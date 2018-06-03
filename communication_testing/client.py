import sys
from socket import socket, AF_INET, SOCK_DGRAM

serverIp   = '192.168.1.144'
portNumber = 5000
buffer = 1024

print("Client sending packets to IP {0}, via port {1}\n".format(serverIp, portNumber))

mySocket = socket(AF_INET, SOCK_DGRAM)
myMessage = "Hello!"
myMessage1 = "Hellow2"
i = 0
while i < 10:
    mySocket.sendto(myMessage.encode('utf-8'), (serverIp, portNumber))
    i = i + 1

mySocket.sendto(myMessage1.encode('utf-8'), (serverIp, portNumber))

sys.exit()
