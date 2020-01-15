import machine
import time
import network
import socket
from boxspecs import Boxspecs as box

led = machine.Pin(2, machine.Pin.OUT)
box()

wifiID = 'VM7873670'
wifiPWD = 'y4kkBmyfvc8q'

#server ip address
IPaddress = "192.168.0.13"
#server port
port = 8090

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(wifiID, wifiPWD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr_info = socket.getaddrinfo(IPaddress, port)
addr = addr_info[0][-1]
