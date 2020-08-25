#!/usr/bin/env python3
import telnetlib
'''
Task 25.1
'''
def transform_topology(new_dict):
    repeated_dict = {}
    for key, value in new_dict.items():
        for key2, value2 in new_dict.items():
            if key == value2 and value == key2:
                if key2 == repeated_dict.get(value2):
                    continue
                else:
                    repeated_dict[key2] = value2
    result = {k: v for k, v in new_dict.items() if k not in repeated_dict}
    return result
topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
class Topology:
    def __init__(self, new_dict):
        repeated_dict = {}
        for key, value in new_dict.items():
            for key2, value2 in new_dict.items():
                if key == value2 and value == key2:
                    if key2 == repeated_dict.get(value2):
                        continue
                    else:
                        repeated_dict[key2] = value2
        result = {k: v for k, v in new_dict.items() if k not in repeated_dict}
        self.topology = result


# top = Topology(topology_example)
# print(top.topology)

'''
Task 25.2
'''

r1_params = {
    'ip': '192.168.122.4',
    'username': 'admin',
    'password': 'password',
    'secret': 'password'}

class CiscoTelnet:
    def __init__(self, dict):
        print('Connection to device {}'.format(dict['ip']))
        with telnetlib.Telnet(dict['ip']) as self.t:
            self.t.read_until(b'Username:')
            self.t.write(b"dict['username']" + b'\n')
            self.t.read_until(b'Password:')
            self.t.write(b"dict['password']" + b'\n')
            self.t.write(b'enable\n')
            self.t.read_until(b'Password:')
            self.t.write(b"dict['secret']" + b'\n')
            self.t.write(b'terminal length 0\n')

    def send_show_command(self, command):
        command = command.encode('ascii')
        print(command)
        self.t.write(command + b'\n')
        return self.t.read_very_eager().decode('ascii')





r1 = CiscoTelnet(r1_params)
print(r1.send_show_command('sh ip int br'))
