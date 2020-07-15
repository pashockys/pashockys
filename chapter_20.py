#!/usr/bin/env python3
from datetime import datetime
import logging
import netmiko
import yaml
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import repeat
import subprocess
import re

if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/exercises/20_concurrent_connections/'):
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/20_concurrent_connections/'
else:
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/20_concurrent_connections/'

'''
examples
'''
'''
logging module
'''
# эта строка указывает, что лог-сообщения paramiko будут выводиться
# только если они уровня WARNING и выше
# logging.getLogger("paramiko").setLevel(logging.WARNING)
#
# logging.basicConfig(
#     format='%(threadName)s %(name)s %(levelname)s: %(message)s',
#     level=logging.INFO)
#
#
# def send_show(device, show):
#     start_msg = '===> {} Connection: {}'
#     received_msg = '<=== {} Received:   {}'
#     ip = device["ip"]
#     logging.info(start_msg.format(datetime.now().time(), ip))
#     start_time = datetime.now()
#     try:
#         with netmiko.ConnectHandler(**device) as ssh:
#             ssh.enable()
#             result = ssh.send_command(show)
#             logging.info(received_msg.format(datetime.now().time(), ip))
#             print(f'executing command "{show}" took {datetime.now()-start_time} on device {ip}')
#             return result
#     except netmiko.ssh_exception.NetmikoAuthenticationException:
#         print('oooooops, wrong password')
#
# def execute_command(devices, command):
#     output = {}
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         result = executor.map(send_show, devices, repeat(command))
#         for res, dev in zip(result, devices):
#             output[dev['ip']] = res
#     return output
# '''
# submit
# '''
# def submit_execute_command(devices, command):
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         future_list = [executor.submit(send_show, device, command) for device in devices]
#         output = {dev['ip']:i.result() for dev, i in zip(devices, as_completed(future_list))}
#     return output
#
# if __name__ == "__main__":
#     with open(path+'my_devices.yaml') as f:
#         devices = yaml.safe_load(f)
    # print(execute_command(devices, 'sh clock'))
    # print(submit_execute_command(devices, 'sh date'))
    # for item, value in submit_execute_command(devices, 'sh date').items():
    #     print(f'For ip {item} was given this result:{value}')

'''
Task 20.1
'''

# logging.basicConfig(format='%(threadName)s %(name)s %(levelname)s: %(message)s', level=logging.INFO)
#
# def actually_ping(ip):
#     result = subprocess.run(f'ping {ip} -c3 -i0.5', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
#     logging.info(result.stdout)
#     return result.returncode, ip
#
# def ping_ip_addresses(ip_list, limit=3):
#     successful_list = []
#     unsuccessful_list = []
#     with ThreadPoolExecutor(max_workers=limit) as executor:
#         future_res = [executor.submit(actually_ping, ip) for ip in ip_list]
#         for i in as_completed(future_res):
#             if i.result()[0] == 0:
#                 successful_list.append(i.result()[1])
#             else:
#                 unsuccessful_list.append(i.result()[1])
#     return (successful_list, unsuccessful_list)
#
# if __name__ == "__main__":
#     with open(path+'my_devices.yaml') as f:
#         devices = yaml.safe_load(f)
#     ip_list = [dev['ip'] for dev in devices]
#     output = ping_ip_addresses(ip_list, 2)
#     print('successful ip:\n{}\nunsuccessful ip:\n{}'.format(output[0], output[1]))

'''
Task 20.2
'''

# def connect_to_ssh(ip_dict, command):
#     ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
#     try:
#         with netmiko.ConnectHandler(**ip_dict)as ssh:
#             ssh.enable()
#             result = [ansi_escape.sub('', ssh.send_command(command)), ssh.find_prompt()]
#             return result
#     except netmiko.ssh_exception.NetmikoAuthenticationException:
#         print(f'wrong password at {ip_dict["ip"]}')
#     except netmiko.ssh_exception.NetmikoTimeoutException:
#         print(f'no connection to {ip_dict["ip"]} (timeout)')
#
# def send_show_command_to_devices(devices, command, filename, limit=3):
#     with open(path + filename+'.txt', 'w') as f:
#         with ThreadPoolExecutor(max_workers=limit) as executor:
#             result = executor.map(connect_to_ssh, devices, repeat(command))
#         for i, res in zip(devices, result):
#             if res:
#                 f.write(res[1]+command+res[0]+'\n')
#                 print(f'info about {i["ip"]} has been written')
#
# if __name__ == "__main__":
#     with open(path+'my_devices.yaml', 'r') as f:
#         devices_dict = yaml.safe_load(f)
# command = 'sh date'
# send_show_command_to_devices(devices_dict, command, 'zalupa', 2)

'''
Task 20.3
'''
# ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
# commands = {'192.168.1.2': 'sh ip int',
#             '192.168.1.3': 'sh arp',
#             '192.168.1.4': 'sh ip int',
#             '192.168.1.5': 'sh arp'}
# # commands = {'192.168.1.2': 'sh ip int br',
# #             '192.168.1.3': 'sh arp',
# #             '192.168.1.4': 'sh ip int br',
# #             '192.168.1.5': 'sh arp'}
#
# def execute_command_by_ssh(device_dict, command):
#     try:
#         with netmiko.ConnectHandler(**device_dict) as ssh:
#             ssh.enable()
#             # result = ssh.find_prompt() + '\n' + ansi_escape.sub('', ssh.send_command(command) + '\n')
#             result = ssh.find_prompt() + ansi_escape.sub('', ssh.send_command(command) + '\n')
#             return result
#     except netmiko.ssh_exception.NetmikoAuthenticationException:
#         print(f'wrong password at {device_dict["ip"]}')
#     except netmiko.ssh_exception.NetmikoTimeoutException:
#         print(f'no connection to {device_dict["ip"]} (timeout)')
#
#
# def send_command_to_devices(devices, commands_dict, filename, limit=3):
#     with open(path+filename, 'w')as f:
#         with ThreadPoolExecutor(max_workers=limit) as executor:
#             future_result = [executor.submit(execute_command_by_ssh, device, commands_dict[device["ip"]]) for device in devices]
#         for res in as_completed(future_result):
#             try:
#                 f.write(res.result())
#             except TypeError:
#                 f.write('pfffff\n')
#
#
# if __name__ == "__main__":
#     with open(path+'my_devices.yaml', 'r') as f:
#         from_file = yaml.safe_load(f)
#
# send_command_to_devices(from_file, commands, 'zalupa3', 2)

'''
Task 20.4
'''
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
def execute_show_command(devices_dict, command):
    try:
        with netmiko.ConnectHandler(**devices_dict) as ssh:
            ssh.enable()
            result = ssh.find_prompt() + ansi_escape.sub('', ssh.send_command(command) + '\n')
            return result
    except netmiko.ssh_exception.NetmikoAuthenticationException:
        print(f'wrong password at {devices_dict["ip"]}')
    except netmiko.ssh_exception.NetmikoTimeoutException:
        print(f'no connection to {devices_dict["ip"]} (timeout)')


def execute_conf_command(devices_dict, commands):
    try:
        with netmiko.ConnectHandler(**devices_dict) as ssh:
            ssh.enable()
            result = ssh.find_prompt() + ansi_escape.sub('', ssh.send_config_set(commands) + '\n')
            return result
    except netmiko.ssh_exception.NetmikoAuthenticationException:
        print(f'wrong password at {devices_dict["ip"]}')
    except netmiko.ssh_exception.NetmikoTimeoutException:
        print(f'no connection to {devices_dict["ip"]} (timeout)')


def send_commands_to_devices(devices, filename, show=None, config=None, limit=3):
    with open(path+filename, 'w')as f:
        with ThreadPoolExecutor(max_workers=limit) as executor:
            if show:
                result = executor.map(execute_show_command, devices, repeat(show))
            if config:
                result = executor.map(execute_conf_command, devices, repeat(config))
            for i in result:
                if i:
                    f.write(i)


if __name__ == '__main__':
    with open(path+'my_devices.yaml', 'r') as f:
        out_from_file = yaml.safe_load(f)
    commands = ['do sh arp', 'do sh date']
    # send_commands_to_devices(devices=out_from_file, filename='zalupa4.txt', show='sh date', limit=2)
    send_commands_to_devices(devices=out_from_file, filename='zalupa4', config=commands, limit=2)

