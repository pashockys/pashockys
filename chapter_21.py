#!/usr/bin/env python3
from jinja2 import Template, Environment, FileSystemLoader
import os
import yaml
import re
if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/exercises/21_jinja2/'):
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/21_jinja2/'
else:
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/21_jinja2/'

'''
Examples
'''
# template = Template('''
# hostname {{name}}
# !
# interface Loopback255
#  description Management loopback
#  ip address 10.255.{{id}}.1 255.255.255.255
# !
# interface GigabitEthernet0/0
#  description LAN to {{name}} sw1 {{int}}
#  ip address {{ip}} 255.255.255.0
# !
# router ospf 10
#  router-id 10.255.{{id}}.1
#  auto-cost reference-bandwidth 10000
#  network 10.0.0.0 0.255.255.255 area 0
# ''')
#
# liverpool = {
#     'id': '11',
#     'name': 'Liverpool',
#     'int': 'Gi1/0/17',
#     'ip': '10.1.1.10'
# }
#
# print(template.render(liverpool))
#
# zalupa_template = Template('pispis insert {{something}} in vagina')
# dict_to_insert = {'something'
#                   ''
#                   '': 'penis'}
# print(zalupa_template.render(dict_to_insert))

'''
Task 21.1
'''

def generate_config(template, data_dict):
    match = re.search('(\S+)/(\S+)', template)
    env = Environment(loader=FileSystemLoader(match.group(1)))
    template = env.get_template(match.group(2))
    out = template.render(data_dict)
    return out

with open(path+'data_files/for.yml') as f:
    data_dict = yaml.safe_load(f)
path_to_template = path+"templates/for.txt"
print(generate_config(path_to_template, data_dict))

'''
Task 21.2
'''


