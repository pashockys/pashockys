#!/usr/bin/env python3
from datetime import datetime
import logging
import netmiko
import yaml
import os

if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/exercises/20_concurrent_connections/'):
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/20_concurrent_connections/'
else:
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/20_concurrent_connections/'

# эта строка указывает, что лог-сообщения paramiko будут выводиться
# только если они уровня WARNING и выше
logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


def send_show(device, show):
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received:   {}'
    ip = device["ip"]
    logging.info(start_msg.format(datetime.now().time(), ip))

    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result =  ssh.send_command(show)
        logging.info(received_msg.format(datetime.now().time(), ip))
    return result

if __name__ == "__main__":
    with open(path+'my_devices.yaml') as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_show(dev, 'sh clock'))