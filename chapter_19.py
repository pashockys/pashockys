#!/usr/bin/env python3
import getpass
import sys
from netmiko import ConnectHandler

command = sys.argv[1]
password = getpass.getpass()
print(password)

user = input('Username: ')
password = getpass.getpass()
enable_pass = getpass.getpass(prompt='Enter enable password: ')

device_ip = '192.168.122.2'

print('connection to device {}'.format(device_ip))
device_params = {
    'device_type': 'cisco_ios',
    'ip': device_ip,
    'username': user,
    'password': password,
    'secret': enable_pass}

with ConnectHandler(**device_params) as ssh:
    ssh.enable()
    result = ssh.send_command(command)
    print(result)



