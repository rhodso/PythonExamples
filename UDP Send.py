#Imports
import socket, time, datetime

#Vars
UDP_IP = "192.168.1.131"
UDP_PORT = 5005
MESSAGE = "Here's some text"

#Print out target information
print("Target information:")
print("IPv4 Address:    " + UDP_IP)
print("Port number:     " + UDP_PORT)
print("Ready to trasnmit...")

#Setup socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Transmit
sock.sendto(bytes(MESSAGE, "UTF-8"), (UDP_IP, UDP_PORT))

#Tell the user the data was sent
print("Sent packet at " + str(datetime.datetime.now()))