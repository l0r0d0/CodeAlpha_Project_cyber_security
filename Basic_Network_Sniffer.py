from scapy.all import sniff, TCP, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"IP Packet: {ip_src} -> {ip_dst}")

    if packet.haslayer(TCP):
        tcp_sport = packet[TCP].sport
        tcp_dport = packet[TCP].dport
        print(f"TCP Packet: {tcp_sport} -> {tcp_dport}")

# Sniff network packets
print("Starting network sniffer...")
sniff(prn=packet_callback, store=0)
