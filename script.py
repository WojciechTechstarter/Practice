# import socket
# hostname = "example.com"
# ip_address = socket.gethostbyname(hostname)
# print(f"Die IP-Adresse von {hostname} ist {ip_address}")'


import ipaddress
network = ipaddress.ip_network("192.168.10.0/24")
print(f"Netzwerk: {network}")
print(f"Erste IP: {network[0]}")
print(f"Letzte IP: {network[-1]}")
print(f"Anzahl nutzbarer Hosts: {network.num_addresses - 2}")