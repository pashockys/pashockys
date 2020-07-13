#!/usr/bin/env python3
from datetime import datetime
import logging
import netmiko
import yaml
import os
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

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
logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


def send_show(device, show):
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received:   {}'
    ip = device["ip"]
    logging.info(start_msg.format(datetime.now().time(), ip))
    start_time = datetime.now()
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(show)
            logging.info(received_msg.format(datetime.now().time(), ip))
            print(f'executing command "{show}" took {datetime.now()-start_time} on device {ip}')
            return result
    except netmiko.ssh_exception.NetmikoAuthenticationException:
        print('oooooops')

def execute_command(devices, command):
    output = {}
    with ThreadPoolExecutor(max_workers=3) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for res, dev in zip(result, devices):
            output[dev['ip']] = res
    return output


if __name__ == "__main__":
    with open(path+'my_devices.yaml') as f:
        devices = yaml.safe_load(f)
    for items, values in execute_command(devices, 'sh date').items():
        print(items, values)