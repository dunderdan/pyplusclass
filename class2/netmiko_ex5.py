#!/usr/bin/env python
"""
5. On both the NXOS1 and NXOS2 switches configure five VLANs including VLAN names 
(just pick 5 VLAN numbers between 100 - 999). Use Netmiko's send_config_from_file() 
method to accomplish this. Also use Netmiko's save_config() method to save the changes 
to the startup-config.
"""
from getpass import getpass
from netmiko import ConnectHandler


password = getpass()

nxos1_device = {
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_nxos',
}

nxos2_device = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_nxos',
}

for device in (nxos1_device, nxos2_device):
    net_connect = ConnectHandler(**device)
    # print(net_connect.find_prompt())
    output = net_connect.send_config_from_file(config_file='vlans.txt')
    output += net_connect.save_config()
    print(output)

net_connect.disconnect()
