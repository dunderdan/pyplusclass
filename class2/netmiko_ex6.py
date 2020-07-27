#!/usr/bin/env python
"""
6. Using SSH and netmiko connect to the Cisco4 router. In your device definition, specify both an 'secret' and a 'session_log'. Your device definition should look as follows:
​password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}
Execute the following sequence of events using Netmiko:
a. Print the current prompt using find_prompt()

b. Execute the config_mode() method and print the new prompt using find_prompt()

c. Execute the exit_config_mode() method and print the new prompt using find_prompt()

d. Use the write_channel() method to send the 'disable' command down the SSH channel. Note, write_channel is a low level method so it requires that you add a newline to the end of your 'disable' command.

e. time.sleep for two seconds and then use the read_channel() method to read the data that is currently available on the SSH channel. Print this to the screen.

f. Execute the enable() method and print your now current prompt using find_prompt(). The enable() method will use the 'secret' defined in your device definition. This 'secret' is the same as the standard lab password.

g. After you are done executing your script, look at the 'my_output.txt' file to see what is included in the session_log.
"""
from getpass import getpass
from netmiko import ConnectHandler
import time

password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}
net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

# Enter configuration mode
print('-' * 25, 'Enter Configuration Mode', '-' * 25)
net_connect.config_mode()
print(net_connect.find_prompt())

# Exit configuration mode
print('-' * 25, 'Exit Configuration Mode', '-' * 25)
net_connect.exit_config_mode()
print(net_connect.find_prompt())

# Exit priviledged exec 
print('-' * 25, 'Exit Priviledged Exec', '-' * 25)
net_connect.write_channel('disable\n')
print(net_connect.find_prompt())
time.sleep(2)
output = net_connect.read_channel()
print(output)

# Enter priviledged exec again
print('-' * 25, 'Enter Priviledged Exec Again', '-' * 25)
net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()
print('Disconnected')
