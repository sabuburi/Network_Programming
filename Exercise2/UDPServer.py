from socket import *
from datetime import datetime

serverPort = 12221 # Port number of your server
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive!")

while True:
    print("-----------------------")
    now = datetime.now()
    receivedMessage,clientAddress = serverSocket.recvfrom(2048)
    seqNum = receivedMessage[0]
    message = receivedMessage[1:]
    print("Received message: " + str(message.decode()))
    print("Sequence Number: " + str(int(seqNum)))
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage + (" | " + str(now.time())).encode(), clientAddress)
    print("Sent message: " + str(modifiedMessage.decode()))
    print(clientAddress[0])
    print(clientAddress[1])
    print(str(now.time()))
    
    