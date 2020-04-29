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

# tuple unpacking
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

# List comprehensions

sizes_of_penis = [size for size in range(10)]
print(sizes_of_penis)

only_true_digits = [true_digit for list in table for true_digit in list if true_digit.isdigit()]
print(only_true_digits)

s = 'abc'
t = (10, 20, 30)
print(dict(zip(s, t)))
