#!/usr/bin/env python3
from textfsm import clitable
import telnetlib
import os

topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

topology_example2 = {('R11', 'Eth0/0'): ('SW12', 'Eth0/1'),
                    ('R21', 'Eth0/0'): ('SW12', 'Eth0/2'),
                    ('SW11', 'Eth0/3'): ('R32', 'Eth0/0')}


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, new_dict):
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
        return result

    def __add__(self, other):
        sum = {}
        sum.update(self.topology)
        sum.update(other.topology)
        return Topology(sum)

    def __iter__(self):
        list_of_dicts = [(item, key) for item, key in self.topology.items()]
        return iter(list_of_dicts)

'''
task 26.1
'''
# top = Topology(topology_example)
# top2 = Topology(topology_example2)
# print(f'at first\n{top.topology}\nand\n{top2.topology}')
# top3 = top + top2
# print(f"zalupa\n{top3.topology}")
# print(f'then\n{top.topology}\nand\n{top2.topology}')
'''
task 26.1a
'''

# top = Topology(topology_example)
# print(f'this is dict\n{top.topology}')
# for i in top:
#     print(i)

'''
task 26.2
'''
if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/exercises/22_textfsm/'):
    path_to_templates = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/22_textfsm/templates'
else:
    path_to_templates = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/22_textfsm/templates'
r1_params = {
    'ip': '192.168.122.11',
    'username': 'admin',
    'password': 'password',
    'secret': 'password'}
attributes = {'Command': 'show ip int br'}


class CiscoTelnet:
    def __init__(self, username, password, secret, ip):
        username = username.encode('ascii')
        password = password.encode('ascii')
        enable_pass = secret.encode('ascii')
        print('Connection to device {}'.format(ip))
        self.t = telnetlib.Telnet(ip)
        self.t.read_until(b'Username:')
        self.t.write(username + b'\n')
        self.t.read_until(b'Password:')
        self.t.write(password + b'\n')
        self.t.write(b'enable\n')
        self.t.read_until(b'Password:')
        self.t.write(enable_pass + b'\n')

    def __enter__(self):
        print('enter method')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit method')
        self.t.close()

    def _write_line(self, command):
        command = command.encode('ascii')
        return command

    def send_show_command(self, command, path_to_templates, parse=False):
        self.t.read_until(b'R4#')
        self.t.write(self._write_line(command) + b'\n')
        if parse:
            output = {}
            out = []
            text_to_parse = self.t.read_until(b'R4#').decode('ascii')
            cli_table = clitable.CliTable('index', path_to_templates)
            cli_table.ParseCmd(text_to_parse, attributes)
            for g in cli_table:
                for i, item in enumerate(cli_table.header):
                    output[item] = g[i]
                out.append(output.copy())
            print(out)
        else:
            print(self.t.read_until(b'R4#').decode('ascii'))

    def send_config_commands(self, list_of_commands):
        self.t.read_until(b'R4#').decode('ascii')
        self.t.write(b'configure terminal\n')
        if type(list_of_commands) is list:
            for i in list_of_commands:
                self.t.write(self._write_line(i) + b'\n')
        else:
            self.t.write(self._write_line(list_of_commands) + b'\n')
        self.t.write(b'end\n')
        print(self.t.read_until(b'R4#').decode('ascii'))
        self.t.write(b'end\n')


# r1 = CiscoTelnet(**r1_params)
# r1.send_show_command('sh ip int br', path_to_templates, parse=False)

with CiscoTelnet(**r1_params) as r1:
    r1.send_show_command('sh ip int br', path_to_templates, parse=False)
