#!/usr/bin/env python
"""
2. Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2. 
Execute 'show lldp neighbors detail' and print the returned output to standard output. 
Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. 
Print the output of this command to standard output. Use the Python datetime library to record the 
execution time of both of these commands. Print these execution times to standard output.
"""
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler

nxos_device = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
    'global_delay_factor': 2,
}

command = 'show lldp neighbors'


net_connect = ConnectHandler(**nxos_device)
# print(net_connect.find_prompt())
start_time = datetime.now()
output = net_connect.send_command(command)
end_time = datetime.now()
print('-' * 70)
print(f'Start time: {start_time}')
print(output)
print(f'End time: {end_time}')
print('-' * 70)

print('-' * 70)
start_time = datetime.now()
output2 = net_connect.send_command(command, delay_factor=8)
end_time = datetime.now()
print(f'Start time: {start_time}')
print(output2)
print(f'End time: {end_time}')
print()
net_connect.disconnect()
