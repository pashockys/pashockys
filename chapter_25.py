#!/usr/bin/env python3
import telnetlib
import textfsm
from tabulate import tabulate
from textfsm import clitable
import os
'''
Task 25.1abcd
'''

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

    def delete_link(self, pair1, pair2):
        print(f"trying to delete {pair1} {pair2}  or {pair2} {pair1} link ")
        if self.topology.get(pair1) is not None and self.topology[pair1] == pair2:
            del self.topology[pair1]
            print(f'deleting link {pair1}{pair2} was successful')
        elif self.topology.get(pair2) is not None and self.topology[pair2] == pair1:
            del self.topology[pair2]
            print(f'deleting link {pair2}{pair1} was successful')
        else:
            print(f"there are no item with {pair1}{pair2} keys")

    def delete_node(self, node):
        node = node.upper()
        dict_after_all = {}
        for key, value in self.topology.items():
            if node == key[0] or node == value[0] or node == key[1] or node == value[1]:
                pass
            else:
                dict_after_all[key] = value
        if dict_after_all != self.topology:
            print(f'there is yout dict after deleting {node}')
            self.topology = dict_after_all
        else:
            print(f'there is no such object like {node}')

    def add_link(self, link1, link2):
        if self.topology.get(link1) is not None:
            print(f'there is link in dict with key {link1} already')
        elif self.topology.get(link2) is not None:
            print(f'there is link in dict with {link2} already')
        else:
            print(f'adding {link1}{link2}')
            self.topology[link1] = link2



# top = Topology(topology_example)
# print(f'at first\n{top.topology}')
# top.delete_link(('R9', 'Eth0/0'), ('R3', 'Eth0/1'))
# top.delete_node('r2')
# top.add_link(('R8', 'Eth0/0'), ('R9', 'Eth0/0'))
# print(f'then\n{top.topology}')

'''
Task 25.2abc
'''
if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/exercises/22_textfsm/'):
    path_to_templates = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/22_textfsm/templates'
else:
    path_to_templates = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/22_textfsm/templates'

r1_params = {
    'ip': '192.168.122.4',
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
    def _write_line(self, command):
        command = command.encode('ascii')
        return command

    def send_show_command(self, command, path_to_templates, parse=False):
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


r1 = CiscoTelnet(**r1_params)
r1.send_show_command('sh ip int br', path_to_templates, parse=True)
# r1.send_config_commands('logging 10.1.1.1')
# r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])