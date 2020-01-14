



for i in range(5):
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.2)

#addr_info = socket.getaddrinfo("10.42.0.144", 8090)
print("marker")
#print(socket.gethostbyname(socket.gethostname()))


addr_info = socket.getaddrinfo("192.168.0.13", 8090)
print(addr_info)

addr = addr_info[0][-1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(addr)
# get local machine name

print("host")
#print(host)



msg = 'Thank you for connecting'+ "\r\n"
s.send(msg.encode('ascii'))

s.close()

#port = 8090
#host = "slim-brick"
#s.connect((host, port))

#print('here!')
