#!/usr/bin/python3
from scapy.all import *

dip="10.0.2.7"
ip1 = IP(dst=dip,id=1000,frag=0,flags=1,proto=17)
udp = UDP(sport=7070,dport=9090,len=96)

payload1="A"*56
print ("Packet No #" + str(1) +" was sent")
print ("=========================================")
pkt = ip1/udp/payload1
pkt[UDP].chksum = 0
send(pkt, verbose=0)

payload2="B"*8
print ("Packet No #" + str(2) +" was sent")
print ("=========================================")
ip2 = IP(dst=dip,id=1000,frag=4,flags=1,proto=17)
pkt = ip2/udp/payload2
send(pkt, verbose=0)

payload3="C"*32
print ("Packet No #" + str(3) +" was sent")
print ("=========================================")
ip3 = IP(dst=dip,id=1000,frag=7,flags=0,proto=17)
pkt = ip3/udp/payload3
send(pkt, verbose=0)
