#!/usr/bin/env python3
import sys
import textfsm
from tabulate import tabulate
import os
if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/exercises/22_textfsm/'):
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/22_textfsm/'
else:
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/22_textfsm/'

template = sys.argv[1]
file_to_parse = sys.argv[2]

with open(path+template, 'r') as template, open(path+file_to_parse, 'r') as file_to_parse:
    fsm = textfsm.TextFSM(template)
    header = fsm.header
    result = fsm.ParseText(file_to_parse.read())
    print(result)
    print(tabulate(result, headers=header))



