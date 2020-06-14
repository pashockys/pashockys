#!/usr/bin/env python3
import re
import os


# task 15.1
# def get_ip_from_cfg(filename):
#     if os.path.exists(
#             '/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename):
#         path = ('/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename)
#     else:
#         path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/15_module_re/'+filename
#     with open(path, 'r')as f:
#         match = re.findall('ip address (\w+\.\w+\.\w+\.\w+) (\w+\.\w+\.\w+\.\w+)', f.read())
#         return match


# task 15.1a
# def get_ip_from_cfg(filename):
#     if os.path.exists(
#             '/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename):
#         path = ('/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename)
#     else:
#         path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/15_module_re/'+filename
#     out_dict = {}
#     with open(path, 'r')as f:
#         for line in f.readlines():
#             match = re.search(r'interface (?P<interface>\S+ *\S*)|'
#                               r'ip address (?P<ip>\w+\.\w+\.\w+\.\w+) (?P<mask>\w+\.\w+\.\w+\.\w+)', line.strip())
#             if match:
#                 if match.lastgroup == 'interface':
#                     interface = match.group('interface')
#                 if match.lastgroup == 'mask':
#                     out_dict[interface] = (match.group('ip'), match.group('mask'))
#         return out_dict


# task 15.1b
def get_ip_from_cfg(filename):
    if os.path.exists(
            '/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename):
        path = ('/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename)
    else:
        path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/15_module_re/'+filename
    out_dict = {}
    with open(path, 'r')as f:
        for line in f.readlines():
            match = re.search(r'interface (?P<interface>\S+ *\S*)|'
                              r'ip address (?P<ip>\w+\.\w+\.\w+\.\w+) (?P<mask>\w+\.\w+\.\w+\.\w+)', line.strip())
            if match:
                if match.lastgroup == 'interface':
                    interface = match.group('interface')
                if match.lastgroup == 'mask':
                    try:
                        out_dict[interface]
                    except KeyError:
                        out_dict[interface] = []
                    out_dict[interface].append((match.group('ip'), match.group('mask')))
        return out_dict


# task 15.2
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


# task 15.3
def convert_ios_nat_to_asa(ios_rules, asa_rules):
    if os.path.exists(
            '/home/pashockys/progi_python/pyneng-examples-exercises/exercises_for_test/15_module_re/'+ios_rules):
        path = ('/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/')
    else:
        path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/15_module_re/'
    with open(path+ios_rules, 'r')as f, open(path+asa_rules, 'w')as f_asa:
        asa_template = '''
object network LOCAL_{ip}
 host {ip}
 nat (inside,outside) static interface service tcp {inside_port} {outside_port}'''
        regex = re.compile('tcp (?P<ip>\S+) (?P<inside_port>\S+) \S+ \S+ (?P<outside_port>\S+)')
        for line in f:
            match = regex.search(line)
            f_asa.write(asa_template.format(ip=match.group('ip'),
                                            inside_port=match.group('inside_port'),
                                            outside_port=match.group('outside_port')))


# task 15.4
def get_ints_without_description(filename):
    out_list = []
    if os.path.exists(
            '/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename):
        path = ('/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename)
    else:
        path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/15_module_re/'+filename
    with open(path, 'r')as f:
        match = re.finditer(r'!\ninterface (\S+)\n (?!description)', f.read())
        for i in match:
            out_list.append(i.group(1))
    return out_list


# task 15.5
def generate_description_from_cdp(filename):
    if os.path.exists(
            '/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename):
        path = ('/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/15_module_re/'+filename)
    else:
        path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/15_module_re/'+filename
    regex = re.compile(r'(?P<device>\S+) {2,}'
                       r'(?P<local_int>\S+ *\S*) {2,}\d+ {2,}\S+ *\S* *\S* {2,}\S+ {2,}'
                       r'(?P<outside_interface>\S+ *\S*)')
    template = 'description Connected to {device} port {outside_interface}'
    with open(path, 'r')as f:
        match = regex.finditer(f.read())
        out_dict = {i.group('local_int'):template.format(device=i.group('device'),
                                                         outside_interface=i.group('outside_interface')) for i in match}
    return out_dict

# print(get_ip_from_cfg('config_r2.txt'))
print(parse_sh_ip_int_br('sh_ip_int_br.txt'))
# convert_ios_nat_to_asa('cisco_nat_config.txt', 'cisco_asa_config.txt')
# print(get_ints_without_description('config_r1.txt'))
# print(generate_description_from_cdp('sh_cdp_n_sw1.txt'))

