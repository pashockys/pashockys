#!/usr/bin/env python3
import getpass
import sys
from netmiko import ConnectHandler
import netmiko
import yaml
import os

if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/exercises/19_ssh_telnet/'):
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/19_ssh_telnet/'
else:
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/19_ssh_telnet/'

'''
Task 19.1a
'''
def send_show_command(device, command):
    print('connection to device {}'.format(device['ip']))
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
    except netmiko.ssh_exception.NetmikoAuthenticationException as er:
        print('please, ensure, that your password is valid\n',er)
        result = None
    except netmiko.ssh_exception.NetmikoTimeoutException as er:
        print('please, ensure that ip address is correct\n', er)
        result = None
    return result

command = sys.argv[1]
user = input('Username: ')
password = getpass.getpass(prompt='ssh password: ')
enable_pass = getpass.getpass(prompt='Enter enable password: ')

# device_ip = '192.168.122.2'
device_ip = '192.168.1.5'

device_params = {
    'device_type': 'cisco_ios',
    'ip': device_ip,
    'username': user,
    'password': password,
    'secret': enable_pass}

print(send_show_command(device_params, command))

'''
Task 19.2
'''
def send_config_commands(device, config_commands):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('connection to device {}'.format(device['ip']))
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    with ConnectHandler(**device) as ssh:
        result = ssh.send_config_set(config_commands)
        print(result)
    return result

# router_vendor = input('enter vendor who are you working with: ')
# commands = ['do sh run int', 'do sh date', 'do sh syslog']
# if router_vendor == 'eltex':
#     with open(path + 'my_devices.yaml') as f:
#         list_of_conf_dict = yaml.safe_load(f)
# else:
#     ip = ['192.168.122.2']
#     enable_password = getpass.getpass(prompt='enable pass: ')
# for i in list_of_conf_dict:
    # print(send_config_commands(i, commands))

'''
Task 19.3
'''

def send_commands(device, show=None, config=None):
    if show:
        result = send_show_command(device, show)
    elif config:
        result = send_config_commands(device, config)
    return result

commands = ['do sh run int', 'do sh date', 'do sh syslog']
with open(path + 'my_devices.yaml') as f:
    list_of_conf_dict = yaml.safe_load(f)
# for i in list_of_conf_dict:
    # # print(send_commands(i, show='sh run interfaces'))
    # print(send_commands(i, config=commands))
