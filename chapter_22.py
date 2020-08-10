#!/usr/bin/env python3
import sys
import textfsm
from tabulate import tabulate
from textfsm import clitable
import os
if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/exercises/22_textfsm/'):
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/22_textfsm/'
else:
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/22_textfsm/'

# template = sys.argv[1]
# file_to_parse = sys.argv[2]
#
# with open(path+template, 'r') as template, open(path+file_to_parse, 'r') as file_to_parse:
#     fsm = textfsm.TextFSM(template)
#     header = fsm.header
#     result = fsm.ParseText(file_to_parse.read())
#     print(result)
#     print(tabulate(result, headers=header))


'''
Task 22.1a
'''
def parse_command_output(template, command_output):
    with open(path + template, 'r') as template:
        fsm = textfsm.TextFSM(template)
        header = fsm.header
        result = [i for i in fsm.ParseText(command_output)]
        result.insert(0, header)
    return result

def parse_output_to_dict(template, command_output):
    output = {}
    out =[]
    with open(path + template, 'r') as template:
        fsm = textfsm.TextFSM(template)
        header = fsm.header
        result = fsm.ParseText(command_output)
        # print('rerererererer', result)
        for g in result:
            for i, item in enumerate(header):
                output[item] = g[i]
            out.append(output.copy())
    return out

# with open(path + 'output/sh_ip_int_br.txt') as f:
#     output = f.read()
# print(parse_command_output(template='templates/sh_ip_int_br.template', command_output=output))

# with open(path + 'output/sh_ip_int_br.txt') as f:
#     output = f.read()
# print(parse_output_to_dict(template='templates/sh_ip_int_br.template', command_output=output))
'''
Task 22.2
'''

# with open(path + 'output/sh_ip_dhcp_snooping.txt') as f:
#     output = f.read()
# print(parse_command_output(template='templates/sh_ip_dhcp_snooping.template', command_output=output))

'''
Task 22.3
'''

def parse_command_dynamic(command_output, attributes_dict, index_file='index', templ_path='templates'):
    cli_table = clitable.CliTable(index_file, path+templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    print('CLI Table output:\n', cli_table)



attributes = {'Command': 'show ip int br', 'Vendor': 'cisco_ios'}
with open(path + 'output/sh_ip_int_br.txt') as f:
    output = f.read()
print(parse_command_dynamic(attributes_dict=attributes, command_output=output))