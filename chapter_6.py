#!/usr/bin/env python3

'''
task 6.1
'''

# mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
# cisco_mac = []
# for element in mac:
#     cisco_mac.append(element.replace(':', '.'))
# print(cisco_mac)
'''
task 6.2ab
'''


while True:
    raw_address = input('enter ip address like this "10.1.1.1": ')
    set_of_address = set(raw_address)
    # allowed_symbols = set('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
    allowed_symbols = set('0123456789.')
    for i in set_of_address:
        a = False
        if i not in allowed_symbols:
            print("you can use only digits and dot")
            break
        a = True
    if a == False:
        continue
    address = raw_address.split('.')
    if len(address) != 4:
        print('must be 4 octets')
        continue
    for i in range(len(address)):
        a = False
        if int(address[i]) > 255:
            print("you can't type digit more than 255 in octet")
            break
        a = True
    if a == True:
        print('well done, address is correct')
        break
    continue
type = 'unused'
if int(address[0]) >= 1 and int(address[0])<= 223:
    type = 'unicast'
elif int(address[0]) >= 224 and int(address[0])<= 239:
    type = 'multicast'
elif int(address[0]) == 255:
    if int(address[1]) == 255 and int(address[2]) == 255 and int(address[3]) == 255:
        type = 'local broadcat'
elif int(address[0]) == 0:
    if int(address[1]) == 0 and int(address[2]) == 0 and int(address[3]) == 0:
        type = 'unassigned'
print(f"IP-address: {raw_address} is {type}")
'''
task 6.3
'''

# access_template = [
# 'switchport mode access', 'switchport access vlan',
# 'spanning-tree portfast', 'spanning-tree bpduguard enable'
# ]
# trunk_template = [
# 'switchport trunk encapsulation dot1q', 'switchport mode trunk',
# 'switchport trunk allowed vlan'
# ]
# access = {
# '0/12': '10',
# '0/14': '11',
# '0/16': '17',
# '0/17': '150'
# }
# trunk = {
# '0/1': ['add', '10', '20'],
# '0/2': ['only', '11', '30'],
# '0/4': ['del', '17']
# }
# # for intf, vlan in access.items():
# #     print('interface FastEthernet' + intf)
# #     for command in access_template:
# #         if command.endswith('access vlan'):
# #             print(' {} {}'.format(command, vlan))
# #         else:
# #             print(' {}'.format(command))
# for intf, vlan in trunk.items():
#     print('interface FastEthernet' + intf)
#     for command in trunk_template:
#         if command.endswith('allowed vlan'):
#             if vlan[0] == 'add':
#                 print(' {} add {}'.format(command, ', '.join(vlan[1:])))
#             elif vlan[0] == 'only':
#                 print(' {} {}'.format(command, ', '.join(vlan[1:])))
#             else:
#                 print(' {} remove {}'.format(command, vlan[1]))


