#!/usr/bin/env python3
import re
import os


def get_ip_from_cfg(filename):
    if os.path.exists(
            '/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename):
        path = ('/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename)
    else:
        path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/15_module_re/'+filename
    with open(path, 'r')as f:
        match = re.findall('ip address (\w+\.\w+\.\w+\.\w+) (\w+\.\w+\.\w+\.\w+)', f.read())
        return match


def parse_sh_ip_int_br(filename):
    out_list = []
    if os.path.exists(
            '/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename):
        path = ('/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename)
    else:
        path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/15_module_re/'+filename
    with open(path, 'r')as f:
        match = re.finditer('(\S+) +(\w+\.\w+\.\w+\.\w+|unassigned) +\S+ +\S+ +(up|down|administratively down) +(\S+)', f.read())
    for i in match:
        out_list.append(i.groups())
    return out_list


print(get_ip_from_cfg('config_r1.txt'))
print(parse_sh_ip_int_br('sh_ip_int_br.txt'))


