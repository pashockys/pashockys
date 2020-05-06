#!/usr/bin/env python3
'''
formatting with f-string
'''
# you can use functions in {}
octets = ['10', '1', '1', '1']
mask = 24
print(f"IP: {'.'.join(octets)}/{mask}")

# you can use formatting
print(f"IP: {'.'.join(octets):8}/{mask:4}")

# sometimes templates a better in format
ip = [10, 1, 1, 1]
oct1, oct2, oct3, oct4 = ip
print(f'{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}')
template = "{:08b} "*4
print(template.format(*ip))

'''
tuple unpacking
'''

interface = ['FastEthernet0/1', 'zalupa', '10.1.1.1', 'up', 'up', 'pizda', 'chlen', 'norm_znachenie']
intf, _, ip, status, protocol, *pisulki, norm = interface
print(ip)
print(pisulki)
print(norm)

table = [
['100', 'a1b2.ac10.7000', 'DYNAMIC', 'Gi0/1'],
['200', 'a0d4.cb20.7000', 'DYNAMIC', 'Gi0/2'],
['300', 'acb4.cd30.7000', 'DYNAMIC', 'Gi0/3'],
['100', 'a2bb.ec40.7000', 'DYNAMIC', 'Gi0/4'],
['500', 'aa4b.c550.7000', 'DYNAMIC', 'Gi0/5'],
['200', 'a1bb.1c60.7000', 'DYNAMIC', 'Gi0/6'],
['300', 'aa0b.cc70.7000', 'DYNAMIC', 'Gi0/7']]
for vlan, mac, _, intf in table:
    print(vlan, mac, intf)

'''
List comprehensions
'''

sizes_of_penis = [size for size in range(10)]
# print(sizes_of_penis)

only_true_digits = [true_digit for list in table for true_digit in list if true_digit.isdigit()]
# print(only_true_digits)

s = 'abc'
t = (10, 20, 30)
# print(dict(zip(s, t)))
'''
Dict comprehensions
'''
# generate dict, where will be key as number and value as sqrt of its number

test_dict = {value: value**2 for value in range(10)}
# print(test_dict)

# now you need to replace all uppercase letters in keys to lowercase
r1 = {'IOS': '15.4',
      'IP': '10.255.0.1',
      'hostname': 'london_r1',
      'location': '21 New Globe Walk',
      'model': '4451',
      'vendor': 'Cisco'}
test_dict_2 = {key.lower(): value for key, value in r1.items() }
# print(test_dict_2)

# the same task as previous one, but you need do to it for several dicts in dict
london_co = {
    'r1' : {
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'IOS': '15.4',
        'IP': '10.255.0.1'
    },
    'r2' : {
        'hostname': 'london_r2',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'IOS': '15.4',
        'IP': '10.255.0.2'
    },
    'sw1' : {
        'hostname': 'london_sw1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'IOS': '3.6.XE',
        'IP': '10.255.0.101'
    }
}

# test_dict_3 = {}
# for device in london_co:
#     test_dict_3[device] = {}
#     for key, value in london_co[device].items():
#         test_dict_3[device][key.lower()] = value

# test_dict_3 = {device: {key.lower(): value for device in london_co} for key, value in london_co[device].items()}
test_dict_3 = {device: {key.lower(): value for key, value in london_co[device].items()} for device in london_co}
# print(test_dict_3)

'''
Working with Dicts
'''
# TASK: you should filter given file so it must show intf only if there are address assigned
try:
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/examples/08_python_basic_examples/sh_ip_int_br.txt'
    open(path, 'r')
except FileNotFoundError:
    print('It seems that you are not at home')
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/examples/08_python_basic_examples/sh_ip_int_br.txt'
with open(path, 'r') as f:
    alpha = [line.strip()  for line in f]
result = {}
for line in alpha[2:]:
    if line.split()[1][0].isdigit():
        intf, ip, *_ = line.split()
        result[intf] = ip
# print(result)

#TASK: in given file you should find interface and MTU and create a dictionary

try:
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/examples/08_python_basic_examples/sh_ip_interface.txt'
    open(path, 'r')
except FileNotFoundError:
    print('It seems that you are not at home')
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/examples/08_python_basic_examples/sh_ip_interface.txt'
with open(path, 'r') as f:
    result_task = {}
    for line in f:
        if 'line protocol' in line:
            interface = line.split()[0]
        if 'MTU' in line:
            result_task[interface] = line.split()[2]
# print(result_task)

#TASK: in given file you should find interface and MTU and IP and create a dict

try:
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/examples/08_python_basic_examples/sh_ip_interface.txt'
    open(path, 'r')
except FileNotFoundError:
    print('It seems that you are not at home')
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/examples/08_python_basic_examples/sh_ip_interface.txt'
with open(path, 'r') as f:
    result_task = {}
    for line in f:
        if 'line protocol' in line:
            interface = line.split()[0]
            result_task[interface] = {}
        if 'Internet address' in line:
            ip = line.split()[-1]
            result_task[interface]['ip'] = ip
        if 'MTU' in line:
            mtu = line.split()[2]
            result_task[interface]['MTU'] = mtu
print(result_task)

