#!/usr/bin/env python3
from sys import argv
'''
task 7.1
'''

# routing_template = '''
# Protocol:           {0}
# Prefix:             {1}
# AD/Metric:          {2}
# Next-Hop:           {3}
# Last update:        {4}
# Outbound Interface: {5}'''
# try:
#     path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/07_files/ospf.txt'
#     open(path, 'r')
# except FileNotFoundError:
#     print('It seems that you are not at home')
#     path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/07_files/ospf.txt'
#
# with open(path, 'r') as f:
#     for line in f:
#         formatted_data = line.split()
#         if formatted_data[0] == 'O':
#             formatted_data[0] = 'OSPF'
#         for element in formatted_data:
#             if element.endswith(','):
#                 formatted_data[formatted_data.index(element)] = element[:-1]
#         print(routing_template.format(formatted_data[0],
#                                       formatted_data[1],
#                                       formatted_data[2],
#                                       formatted_data[4],
#                                       formatted_data[5],
#                                       formatted_data[6]))

'''
task 7.2
'''
# file_to_work_with = argv[1]
# try:
#     path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/07_files/'+file_to_work_with
#     open(path, 'r')
# except FileNotFoundError:
#     print('It seems that you are not at home')
#     path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/07_files/'+file_to_work_with
# with open(path, 'r') as f:
#     for line in f:
#         if line.startswith('!'):
#             continue
#         print(line.strip())
'''
task 7.3
'''
try:
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/07_files/CAM_table.txt'
    open(path, 'r')
except FileNotFoundError:
    print('It seems that you are not at home')
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/07_files/CAM_table.txt'
with open(path, 'r') as f:
    alpha = f.readlines()[6:]
for line in alpha:
    if "DYNAMIC" in line:
        # alpha[alpha.index(line)] = line.replace('DYNAMIC', '').strip()
        print(line.replace('DYNAMIC', '').strip())

# print(alpha)