#!/usr/bin/env python
"""
3. On your AWS lab server, look at the ntc-templates index file (at ~/ntc-templates/templates/index). 
Look at some of the commands available for cisco_ios (you can use 
'cat ~/ntc-templates/templates/index | grep cisco_ios' to see this). 
Also look at some of the abbreviated forms of Cisco IOS commands that are supported in the index file.

Create a script using Netmiko that executes 'show version' and 'show lldp neighbors' against the Cisco4 
device with use_textfsm=True.

What is the outermost data structure that is returned from 'show lldp neighbors' (dictionary, list, 
string, something else)? The Cisco4 device should only have one LLDP entry (the HPE switch that this 
router connects to). From this LLDP data, print out the remote device's interface. In other words, 
print out the port number on the HPE switch that Cisco4 connects into.
"""
from getpass import getpass
from netmiko import ConnectHandler


device = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
}

commands = ['show version', 'show lldp neighbors']

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

for cmd in commands:
    output = net_connect.send_command(cmd, use_textfsm=True)
    print('-' * 60)
    print(f'Output for {cmd}')
    print('-' * 60)
    print(output)
    print('-' * 60)

    if cmd == 'show lldp neighbors':
        print(type(output))
        print(output[0]['local_interface'])
print('Completed running commands')
net_connect.disconnect()
