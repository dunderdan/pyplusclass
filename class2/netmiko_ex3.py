#!/usr/bin/env python
"""
3. On your AWS lab server, look at the ntc-templates index file (at ~/ntc-templates/templates/index). Look at some of the commands available for cisco_ios (you can use 'cat ~/ntc-templates/templates/index | grep cisco_ios' to see this). Also look at some of the abbreviated forms of Cisco IOS commands that are supported in the index file.

Create a script using Netmiko that executes 'show version' and 'show lldp neighbors' against the Cisco4 device with use_textfsm=True.

What is the outermost data structure that is returned from 'show lldp neighbors' (dictionary, list, string, something else)? The Cisco4 device should only have one LLDP entry (the HPE switch that this router connects to). From this LLDP data, print out the remote device's interface. In other words, print out the port number on the HPE switch that Cisco4 connects into.
"""


