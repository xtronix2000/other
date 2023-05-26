import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP or IP range.')
    option = parser.parse_args()
    return option


def scan(ip):
    arp_request_broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')/scapy.ARP(pdst=ip)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list = []
    for ans in answered_list:
        client_list.append({'ip': ans[1].psrc, 'mac': ans[1].hwsrc})
    return client_list


def print_result(result_list):
    print('IP\t\t\tMac Address\n-----------------------------------------')
    for res in result_list:
        print(f"{res['ip']}\t\t{res['mac']}")



options = get_arguments()
result = scan(options.target)
print_result(result)

