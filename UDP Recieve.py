#Imports
import socket, datetime

#Vars
UDP_ID = socket.gethostbyname(socket.gethostname())
UDP_PORT = 5005
Message = ""

#Setup socket
sock = socket.socket.(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_ID, UDP_PORT))

#Loop
while(True):
    #Recieve message
    data, addr, = sock.recvfrom(1024)
    Message = ""

    #Decode message
    for i in range(0, len(data)):
        Message = Message + chr(data[i])

    #Print out message
    print(set(datetime.datetime.now() + "|  ") + Message)
