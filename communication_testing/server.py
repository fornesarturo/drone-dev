import os
from socket import *

buffer = 1024
host = ""
port = 13000
localAddr = (host, port)

UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(localAddr)

print("Waiting to receive messages...")

while True:
    (data, addr) = UDPSock.recvfrom(buffer)
    print("Received message: " + data + "\tFrom: " + addr)
    if data == "exit":
        break

UDPSock.close()
os._exit(0)