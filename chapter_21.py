#!/usr/bin/env python3
from jinja2 import Template, Environment, FileSystemLoader
import os
import netmiko
from concurrent.futures import ThreadPoolExecutor, as_completed
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

# def generate_config(template, data_dict):
#     match = re.search('(\S+)/(\S+)', template)
#     env = Environment(loader=FileSystemLoader(match.group(1)), trim_blocks=True)
#     template = env.get_template(match.group(2))
#     out = template.render(data_dict)
#     return out

# with open(path+'data_files/for.yml') as f:
#     data_dict = yaml.safe_load(f)
# path_to_template = path+"templates/for.txt"
# print(generate_config(path_to_template, data_dict))

'''
Task 21.2
'''

# with open(path+'data_files/router_info.yml') as f:
#     data_dict = yaml.safe_load(f)
# path_to_template = path+"templates/cisco_router_base.txt"
# print(generate_config(path_to_template, data_dict))

'''
Task 21.3
'''

# with open(path+'data_files/ospf.yml') as f:
#     data_dict = yaml.safe_load(f)
# path_to_template = path+"templates/ospf.txt"
# print(generate_config(path_to_template, data_dict))

'''
Task 21.4
'''

# with open(path+'data_files/add_vlan_to_switch.yml') as f:
#     data_dict = yaml.safe_load(f)
# path_to_template = path+"templates/add_vlan_to_switch.txt"
# print(generate_config(path_to_template, data_dict))

'''
Task 21.5
'''

# data = {
#     'tun_num': 10,
#     'wan_ip_1': '192.168.100.1',
#     'wan_ip_2': '192.168.100.2',
#     'tun_ip_1': '10.0.1.1 255.255.255.252',
#     'tun_ip_2': '10.0.1.2 255.255.255.252'
# }
#
# def create_vpn_config(template1, template2, data_dict):
#     path_to_template_1 = path + template1
#     path_to_template_2 = path + template2
#     match = re.search(r'(\S+)/(\S+)', path_to_template_1)
#     env1 = Environment(loader=FileSystemLoader(match.group(1)), trim_blocks=True)
#     out1 = env1.get_template(match.group(2)).render(data_dict)
#     match = re.search(r'(\S+)/(\S+)', path_to_template_2)
#     env2 = Environment(loader=FileSystemLoader(match.group(1)), trim_blocks=True)
#     out2 = env2.get_template(match.group(2)).render(data_dict)
#     return (out1, out2)
#
#
# # print(create_vpn_config("templates/gre_ipsec_vpn_1.txt", "templates/gre_ipsec_vpn_2.txt", data))
# for i in create_vpn_config("templates/gre_ipsec_vpn_1.txt", "templates/gre_ipsec_vpn_2.txt", data):
#     print(i)

'''
Task 21.5a
'''

def configure_vpn(src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
    src_template = path + src_template
    dst_template = path + dst_template
    match = re.search(r'(\S+)/(\S+)', src_template)
    env1 = Environment(loader=FileSystemLoader(match.group(1)), trim_blocks=True)
    out1 = env1.get_template(match.group(2)).render(vpn_data_dict)
    with netmiko.ConnectHandler(**src_device_params) as ssh:
        ssh.enable()
        # ssh.send_command('sh run')
        ssh.send_config_set(out1, delay_factor=60)
    match = re.search(r'(\S+)/(\S+)', dst_template)
    env2 = Environment(loader=FileSystemLoader(match.group(1)), trim_blocks=True)
    out2 = env2.get_template(match.group(2)).render(vpn_data_dict)
    with netmiko.ConnectHandler(**dst_device_params) as ssh:
        ssh.enable()
        # ssh.send_command('sh run')
        ssh.send_config_set(out2)


'''
Создать функцию configure_vpn, которая использует шаблоны из задания 21.5 для настройки VPN на маршрутизаторах на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству
* dst_device_params - словарь с параметрами подключения к устройству
* src_template - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* dst_template - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

'''

data = {
    'tun_num': 1,
    'wan_ip_1': '192.168.122.2',
    'wan_ip_2': '192.168.122.4',
    'tun_ip_1': '10.0.1.1 255.255.255.252',
    'tun_ip_2': '10.0.1.2 255.255.255.252'
}
dev_params = {
  'device_type': 'cisco_ios',
  'ip': '192.168.122.2',
  'username': 'admin',
  'password': 'password',
  'secret': 'password'
}
src_params = {
  'device_type': 'cisco_ios',
  'ip': '192.168.122.4',
  'username': 'admin',
  'password': 'password',
  'secret': 'password'
}

configure_vpn(src_device_params=src_params,
              dst_device_params=dev_params,
              src_template="templates/21_5a_vpn_1.txt",
              dst_template="templates/21_5a_vpn_2.txt",
              vpn_data_dict=data)

