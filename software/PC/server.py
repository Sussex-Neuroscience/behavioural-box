####!/usr/bin/python3           # This is server.py file
import socket
#import network

#station = network.WLAN(network.STA_IF)
#station.active(True)

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

print(socket.gethostbyname(socket.gethostname()))
# get local machine name
#host = socket.gethostname()
#host = socket.gethostbyname(socket.gethostname())
host = '0.0.0.0'
print(host)
port = 8090

#ip_address_v4 = station.ifconfig()[0]
#print(ip_address_v4)
# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)
flag = 1


while True:
   if flag == 1:
	   flag = 0
	   print("here")
   # establish a connection
   clientsocket,addr = serversocket.accept()

   print("Got a connection from %s" % str(addr))

   msg = clientsocket.recv(1024)
   print(msg)
   #msg = 'Thank you for connecting'+ "\r\n"

   #clientsocket.send(msg.encode('ascii'))
   clientsocket.close()
