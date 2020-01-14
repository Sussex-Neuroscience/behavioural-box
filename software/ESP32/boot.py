import machine
import time
import network
import socket




def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('VM7873670', 'y4kkBmyfvc8q')
        #sta_if.connect('slim-brick', 'fishy1234')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
led = machine.Pin(2, machine.Pin.OUT)

#station = network.WLAN(network.STA_IF)
#station.active(True)

#print('here')
#station.connect('slim-brick', 'fishy1234')
#print(station.isconnected())
#ip_address_v4 = station.ifconfig()[0]
#print(ip_address_v4)

#station.connect("zhotspot", "wifijunkie2")

#while not station.isconnected():
#    print("not")
#    station.connect("slim-brick", "fishy1234")


#station.ifconfig()
#print(station.ifconfig())
#print(station.isconnected())




# connection to hostname on the port.
