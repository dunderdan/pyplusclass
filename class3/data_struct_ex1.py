#!/usr/bin/env python
"""
1. Using the below ARP data, create a five element list. Each list element should be a dictionary 
with the following keys: "mac_addr", "ip_addr", "interface". At the end of this process, you should 
have five dictionaries contained inside a single list.

Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""
import re
from pprint import pprint


arp_entries = """
    Protocol  Address      Age  Hardware Addr   Type  Interface
    Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
    Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
    Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
    Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
    Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
    """

arp_entries = arp_entries.strip()
arp = arp_entries.splitlines()

arp_list = []

for entry in arp:
    if re.search(r'Protocol', entry):
        # print(entry)
        continue
    # After the first line work with the rest of the data
    # print(entry)
    _internet, ip_addr, _age, mac_addr, _type_of, interface = entry.split()
    # print(ip_addr)
    arp_dict = {"mac_addr": mac_addr, "ip_addr": ip_addr, "interface": interface}
    arp_list.append(arp_dict)

pprint(arp_list)
