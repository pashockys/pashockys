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
task 5.1abcd
'''

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
# dict_new = input('tell me what dict do you need:\n')
# parameter = input('and what parameter do you need exactly{}\n'.format(london_co[dict_new].keys()))
# print('here is what you wanted:\n{}'.format(london_co[dict_new].get(parameter.lower(), 'hui')))

'''
task 5.2ab
'''

# def dec_to_mask(dec):
#     ones = ''
#     zeros = ''
#     list_result = []
#     for i in range(int(dec)):
#         ones += '1'
#     for i in range(32-int(dec)):
#         zeros += '0'
#     result = ones + zeros
#     for i in range(4):
#         list_result.append(result[i*8:8*i+8])
#     return list_result
#
#
# def host_or_not(mask, address):
#     result_address = ''
#     for i in range(len(address)):
#         result_address += '{0:08b}'.format(int(network_from_preffix[i]))
#     result_after_mask = result_address[int(mask):]
#     if '1' in set(result_after_mask):
#         result_address = result_address[:int(mask)] + '0'*(32 - int(mask))
#         list_result = []
#         for i in range(len(address)):
#             list_result.append(int(result_address[i * 8:8 * i + 8], 2))
#         return list_result
#     return address
#
#
# # preffix = input('tell me your preffix like 10.1.1.0/24\n')
# preffix = argv[1]
#
# ip_template = '''
# {0:<8} {1:<8} {2:<8} {3:<8}
# {0:08b} {1:08b} {2:08b} {3:08b}
# '''
# ip_mask_template = '''/{0}
# {1:<8} {2:<8} {3:<8} {4:<8}
# {1:08b} {2:08b} {3:08b} {4:08b}
# '''
#
# network_from_preffix = preffix.split('/')[0].split('.')
# mask_from_preffix = preffix.split('/')[1]
# print(mask_from_preffix, network_from_preffix)
# vova = '{0:08b}'.format(int(network_from_preffix[0]))
# print(vova)
# network_from_preffix = host_or_not(mask_from_preffix, network_from_preffix)
# print('Network:', ip_template.format(int(network_from_preffix[0]),
#                                      int(network_from_preffix[1]),
#                                      int(network_from_preffix[2]),
#                                      int(network_from_preffix[3])))
# print('Mask:\n', ip_mask_template.format(mask_from_preffix,
#                                           int(dec_to_mask(mask_from_preffix)[0], 2),
#                                           int(dec_to_mask(mask_from_preffix)[1], 2),
#                                           int(dec_to_mask(mask_from_preffix)[2], 2),
#                                           int(dec_to_mask(mask_from_preffix)[3], 2),))

'''
task 5.3a
'''
access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
dict_new = {
    'access': [access_template, 'enter vlan number: '],
    'trunk': [trunk_template, 'please enter allowed vlans: ']
}
mode = input('Введите режим работы интерфейса (access/trunk): ')
type = input("enter type of your interface and it's number: ")
numbers_of_vlans = input(dict_new[mode][1])


print('Interface {}'.format(type))
print('\n'.join(dict_new[mode][0]).format(numbers_of_vlans))

