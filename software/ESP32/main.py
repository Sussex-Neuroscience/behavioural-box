



for i in range(5):
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.2)



s.connect(addr)


msg = 'Thank you for connecting'+ "\r\n"
s.send(msg.encode('ascii'))

s.close()

#port = 8090
#host = "slim-brick"
#s.connect((host, port))

#print('here!')
