#!/usr/bin/env python3
import re
'''
Task 11.1
'''

def parse_cdp_neighbors(command_output):
    list = command_output.split()
    list[0] = list[0][:list[0].find('>')]
    router_from = []
    counter = 0
    router_to = []; local_iface_alpha = []; remote_iface_alpha = []
    for i in range(len(list)):
        if re.search('\d/\d', list[i]) is not None:
            if counter == 0:
                router_to.append(list[i-2])
                local_iface_alpha.append(list[i-1]+list[i])
                router_from.append(list[0])
                counter = 1
                continue
            if counter == 1:
                remote_iface_alpha.append(list[i - 1]+list[i])
                counter = 0
    output_dict = dict(zip(zip(router_from, local_iface_alpha),zip(router_to, remote_iface_alpha)))
    print(output_dict)
    return output_dict



try:
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/11_modules/sh_cdp_n_sw1.txt'
    open(path, 'r')
except FileNotFoundError:
    print('It seems that you are not at home')
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/11_modules/sh_cdp_n_sw1.txt'
with open(path, 'r') as f:
    output_from_file = f.read()


# parse_cdp_neighbors(output_from_file)

'''
Task 11.2
'''
#lies in test, because of using modules