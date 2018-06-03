import os
from socket import *

host = ""
port = 13000
localAddr = (host, port)

UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

print("Waiting to receive messages...")

while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print("Received message: " + data + "\tFrom: " + addr)
    if data == "exit":
        break

UDPSock.close()
os._exit(0)