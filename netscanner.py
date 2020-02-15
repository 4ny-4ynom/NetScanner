import scapy.all as scapy
import optparse

# 1)arp_request
# 2)broadcast
# 3)response

def options():
    inputs = optparse.OptionParser()
    inputs.add_option("-i","--ipaddress",dest="ip_address",help="Enter IP Address")
    (user_input,arguments)= inputs.parse_args()


    if not user_input.ip_address:
        print("Enter IP Address")


    return user_input


def scanner(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    ##scapy.ls(scapy.Ether())

    combine_packet = broadcast_packet / arp_request_packet

    (answered, unanswered) = scapy.srp(combine_packet, timeout=1)

    answered.summary()

try:
    user_ip_address=options()
    scanner(user_ip_address.ip_address)
except:
    print("TRY AGAIN FOR EXAMPLE:\n     python3 netscanner.py -i 192.168.1.0/24")