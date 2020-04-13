'''
task 6.1
'''
# mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
# cisco_mac = []
# for element in mac:
#     cisco_mac.append(element.replace(':', '.'))
# print(cisco_mac)
'''
task 6.2
'''
# raw_address = input('enter ip address like this "10.1.1.1": ')
# address = raw_address.split('.')
#
# type = 'unused'
# if int(address[0]) >= 1 and int(address[0])<= 223:
#     type = 'unicast'
# elif int(address[0]) >= 224 and int(address[0])<= 239:
#     type = 'multicast'
# elif int(address[0]) == 255:
#     if int(address[1]) == 255 and int(address[2]) == 255 and int(address[3]) == 255:
#         type = 'local broadcat'
# elif int(address[0]) == 0:
#     if int(address[1]) == 0 and int(address[2]) == 0 and int(address[3]) == 0:
#         type = 'unassigned'
# print(f"IP-address: {raw_address} is {type}")
'''
task 6.3
'''
access_template = [
'switchport mode access', 'switchport access vlan',
'spanning-tree portfast', 'spanning-tree bpduguard enable'
]
trunk_template = [
'switchport trunk encapsulation dot1q', 'switchport mode trunk',
'switchport trunk allowed vlan'
]
access = {
'0/12': '10',
'0/14': '11',
'0/16': '17',
'0/17': '150'
}
trunk = {
'0/1': ['add', '10', '20'],
'0/2': ['only', '11', '30'],
'0/4': ['del', '17']
}
for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

