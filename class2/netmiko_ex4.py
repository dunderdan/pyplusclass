#!/usr/bin/env python
"""
4. Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.

ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup

Experiment with fast_cli=True to see how long the script takes to execute 
(with and without this option enabled).

Verify DNS lookups on the router are now working by executing 'ping google.com'. 
Verify from this that you receive a ping response back.
"""
from getpass import getpass
from netmiko import ConnectHandler


device = {
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
    'fast_cli': True,
}

commands = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']

net_connect = ConnectHandler(**device)
# print(net_connect.find_prompt())
output = net_connect.send_config_set(commands)
print(output)
print('-' * 60)
verify_dns = net_connect.send_command('ping google.com')
print(verify_dns)
print('-' * 60)
