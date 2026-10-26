from socket import *

seqNum = 1
serverName = '163.143.11.59' # IP address of your server
serverPort = 12221  # Port number of your server
destAddress=(serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    print("-----------------------")
    message = input("Input lowercase sentence:")
    if seqNum <= 9:
        addedMessage = bytes([seqNum]) + message.encode()
    else: 
        addedMessage = message.encode()
    clientSocket.sendto(addedMessage,destAddress)
    print("Sent message: " + str(seqNum) + message)
    receivedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("Received message: " + str(receivedMessage.decode()))
    seqNum += 1 