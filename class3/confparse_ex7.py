#!/usr/bin/env python
"""
7. You have the following BGP configuration from a Cisco IOS-XR router:
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out

From this BGP configuration, retrieve all of BGP peer IP addresses and their corresponding remote-as. 
Return a list of tuples. The tuples should be (neighbor_ip, remote_as). Print your data-structure to 
standard output.

Your output should look similar to the following. Use ciscoconfparse to accomplish this.
​BGP Peers: 
[('10.220.88.20', '42'), ('10.220.88.32', '43')]

"""


