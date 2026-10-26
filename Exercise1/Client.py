from socket import *
import time

starttime = .................. # Use this line for to compute delay

serverName = 'www.server.com' # Use this line for question 1

######DON'T CHANGE THIS PART!!!#######
serverPort = 80
destAddress = (serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(destAddress)
message = "GET / HTTP/1.1\r\nHost:"+serverName+"\r\n\r\n"
# send the request
clientSocket.send(message.encode())
# start to receive the reply. Note: this is just a part of
# the response. We will learn to receive a whole response later 
response = clientSocket.recv(4096).decode()
clientSocket.close()
# finish receiving the reply
######################################


#### Question 1
#print reply message here
....................................


#### Hints

#How to compute the time delay of the above operation. 
#First, please compute starttime, endtime, and timeDelay.  
endtime = .................. # in seconds
timeDelay = .................. # compute the time delay
print("timeDelay: "+str(timeDelay)) # display the time delay


#How to compute the throughput
#The datasize can be obtained by len() function.
#And throughput = datasize/timedelay

