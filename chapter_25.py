#!/usr/bin/env python3
import telnetlib
'''
Task 25.1abc
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
        dict_after_all = {}
        for key, value in self.topology.items():
            if node == key[0] or node == value[0] or node == key[1] or node == value[1]:
                pass
            else:
                dict_after_all[key] = value
        if dict_after_all is not None:
            print(f'there is yout dict after deleting {node}')
            self.topology = dict_after_all
        else:
            print(f'there is no such object like {node}')


top = Topology(topology_example)
print(top.topology)
# top.delete_link(('R4', 'Eth0/0'), ('R3', 'Eth0/1'))
top.delete_node('SW5')
print(top.topology)
'''
Task 25.2
'''

r1_params = {
    'ip': '192.168.122.11',
    'username': 'admin',
    'password': 'password',
    'secret': 'password'}


class CiscoTelnet:
    def __init__(self, dict):
        username = dict['username'].encode('ascii')
        password = dict['password'].encode('ascii')
        enable_pass = dict['secret'].encode('ascii')
        print('Connection to device {}'.format(dict['ip']))
        self.t = telnetlib.Telnet(dict['ip'])
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

    def send_show_command(self, command):
        self.t.read_until(b'R1#')
        self.t.write(self._write_line(command) + b'\n')
        print(self.t.read_until(b'R1#').decode('ascii'))


# r1 = CiscoTelnet(r1_params)
# r1.send_show_command('sh ip int br')

