# app/sniffer.py
from scapy.all import sniff, DNSQR, IP
from .extensions import socketio
from datetime import datetime

def process_packet(packet):
    data = {}
    data['time'] = datetime.now().strftime("%H:%M:%S")
    data['protocol'] = "DNS"

    if packet.haslayer(DNSQR):
        data['domain'] = packet[DNSQR].qname.decode()[:-1]
    else:
        data['domain'] = "Unknown"

    if packet.haslayer(IP):
        data['ip'] = packet[IP].src
    else:
        data['ip'] = "Unknown"

    print(f"Captured: {data}")
    socketio.emit('packet', data)

def start_sniffing():
    sniff(filter="udp port 53", prn=process_packet, store=False)
