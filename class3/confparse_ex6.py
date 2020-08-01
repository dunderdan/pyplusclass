#!/usr/bin/env python
"""
6. Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address. 
Print out the interface name and IP address for each interface. Your solution should work if there is more 
than one IP address configured on Cisco4. For example, if you configure a loopback interface on Cisco4 with 
an IP address, then your solution should continue to work. The output from this program should look similar 
to the following:

$ python confparse_ex6.py 

Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0
"""

