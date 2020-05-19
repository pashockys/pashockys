#!/usr/bin/env python3
'''
Task 11.1
'''

def parse_cdp_neighbors(command_output):
    return True



try:
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/11_modules/sh_cdp_n_sw1.txt'
    open(path, 'r')
except FileNotFoundError:
    print('It seems that you are not at home')
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/11_modules/sh_cdp_n_sw1.txt'
with open(path, 'r') as f:
    print(f.read())