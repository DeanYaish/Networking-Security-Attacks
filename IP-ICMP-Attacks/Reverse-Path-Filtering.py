#!/usr/bin/python3
from scapy.all import *

a = IP()
a.dst = '192.168.60.5'
b = ICMP()

a.src = '10.0.2.45'
payload1 = 'A'
p1 = a/b/payload1
print ("Packet No #" + str(1) +" was sent")
print ("=========================================")
send(p1)

a.src = '192.168.60.13'
payload2 = 'B'
p2 = a/b/payload2
print ("Packet No #" + str(2) +" was sent")
print ("=========================================")
send(p2)

a.src = '98.138.11.157'
payload3 = 'C'
p3 = a/b/payload3
print ("Packet No #" + str(3) +" was sent")
print ("=========================================")
send(p3)