#!/usr/bin/env python3
from netmiko import ConnectHandler
'''
task 6.1
'''

device_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.11',
    'username': 'admin',
    'password': 'password',
    'secret': 'password'
}


def netmiko_ssh(**params_dict):
    ssh = ConnectHandler(**params_dict)
    ssh.enable()
    def send_show_command(command):
        if command == 'close':
            print('connection wad closed')
            return ssh.disconnect()
        try:
            result = ssh.send_command(command)
        except AttributeError:
            print('session was closed')
            return False
        return result
    return send_show_command


# if __name__ == "__main__":
#     r1 = netmiko_ssh(**device_params)
#     print(r1('sh clock'))
#     print(r1('close'))
#     print(r1('sh ip int br'))

'''
task 6.2
'''

def count_total(num):
    sum1 = num
    def inner():
        nonlocal sum1
        sum1 = num + sum1
        return sum1
    return inner

print(f'{count_total(15)()}')
print(f'{count_total(20)()}')