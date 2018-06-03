import os
from socket import *

serverIp = "192.168.1.144" # Server's IP
port = 13000
severAddr = (serverIp, port)

UDPSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input("Enter message to send or type 'exit': ")
    UDPSock.sendto(data, serverAddr)
    if data == "exit":
        break

UDPSock.close()
os._exit(0)