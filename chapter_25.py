#!/usr/bin/env python3
import telnetlib
'''
Task 25.1a
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
# class Topology:
#     def __init__(self, new_dict):
#         repeated_dict = {}
#         for key, value in new_dict.items():
#             for key2, value2 in new_dict.items():
#                 if key == value2 and value == key2:
#                     if key2 == repeated_dict.get(value2):
#                         continue
#                     else:
#                         repeated_dict[key2] = value2
#         result = {k: v for k, v in new_dict.items() if k not in repeated_dict}
#         self.topology = result

#     class Topology:
#         def __init__(self, topology_dict):
#             self.topology = self._normalize(topology_dict)
#
#     def _normalize(self, new_dict):
#         repeated_dict = {}
#             for key, value in new_dict.items():
#                 for key2, value2 in new_dict.items():
#                     if key == value2 and value == key2:
#                         if key2 == repeated_dict.get(value2):
#                             continue
#                         else:
#                             repeated_dict[key2] = value2
#         result = {k: v for k, v in new_dict.items() if k not in repeated_dict}
#         return result
#
#
#
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
        enable_pass = dict['secret'].encode('ascii')
        password = dict['password'].encode('ascii')
        username = dict['username'].encode('ascii')
        print('Connection to device {}'.format(dict['ip']))
        self.t = telnetlib.Telnet(dict['ip'])
        self.t.read_until(b'Username:')
        self.t.write(username + b'\n')
        self.t.read_until(b'Password:')
        self.t.write(password + b'\n')
        self.t.write(b'enable\n')
        self.t.read_until(b'Password:')
        self.t.write(enable_pass + b'\n')
        # self.t.read_until(b'R4#')
            # self.t.write(b'sh ip int br\n')
            # print(self.t.read_until(b'R4#').decode('ascii'))

    def send_show_command(self, command):
        command = command.encode('ascii')
        self.t.read_until(b'R4#')
        self.t.write(command + b'\n')
        print(self.t.read_until(b'R4#').decode('ascii'))





r1 = CiscoTelnet(r1_params)
r1.send_show_command('sh ip int br')









#
# class CiscoTelnet:
#     def __init__(self, dict):
#         enable_pass = dict['secret'].encode('ascii')
#         password = dict['password'].encode('ascii')
#         username = dict['username'].encode('ascii')
#         print('Connection to device {}'.format(dict['ip']))
#         t = telnetlib.Telnet('192.168.100.1')
#         with telnetlib.Telnet(dict['ip']) as self.t:
#             self.t.read_until(b'Username:')
#             self.t.write(username + b'\n')
#             self.t.read_until(b'Password:')
#             self.t.write(password + b'\n')
#             self.t.write(b'enable\n')
#             self.t.read_until(b'Password:')
#             self.t.write(enable_pass + b'\n')
            # self.t.read_until(b'R4#')
            # self.t.write(b'sh ip int br\n')
            # print(self.t.read_until(b'R4#').decode('ascii'))


