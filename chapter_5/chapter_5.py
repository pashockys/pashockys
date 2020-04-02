#!/usr/bin/env python3
from sys import argv
# interface = input('tell me interface:\n')
# vlan_number = argv[1]
# access_template = ['switchport mode access',
#                    'interface {}',
#                    'switchport access vlan {}',
#                    'switchport nonegotiate',
#                    'spanning-tree portfast',
#                    'spanning-tree bpduguard enable']
# print('\n' + '-' * 30)
# print('\n'.join(access_template).format(interface, vlan_number))
'''
task 5.1
'''
# dict_new = input('tell me what dict do you need:\n')
#
# london_co = {
#     'r1': {
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '4451',
#         'ios': '15.4',
#         'ip': '10.255.0.1'
#     },
#     'r2': {
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '4451',
#         'ios': '15.4',
#         'ip': '10.255.0.2'
#     },
#     'sw1': {
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '3850',
#         'ios': '3.6.XE',
#         'ip': '10.255.0.101',
#         'vlans': '10,20,30',
#         'routing': True
#     }
# }
# print(f"here is your dict{london_co[dict_new]}")
'''
task 5.2
'''
# preffix = input('tell me your preffix like 10.1.1.0/24\n')
preffix = '10.1.1.0/24'

ip_template = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
network_from_preffix = preffix.split('/')[0].split('.')
mask_from_preffix = preffix.split('/')[1]
print(network_from_preffix, mask_from_preffix)
print('Network:', ip_template.format(int(network_from_preffix[0]),
                                     int(network_from_preffix[1]),
                                     int(network_from_preffix[2]),
                                     int(network_from_preffix[3])))
print('Mask:\n/', ip_template.format(int(network_from_preffix[0]),
                                     int(network_from_preffix[1]),
                                     int(network_from_preffix[2]),
                                     int(network_from_preffix[3])))
