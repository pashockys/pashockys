#!/usr/bin/env python3
import csv
import json
import os
import re
#######################################
# CSV
#######################################
test_file = '/home/pashockys/progi_python/pyneng-examples-exercises/examples/17_serialization/csv/sw_data.csv'
test_file_json = '/home/pashockys/progi_python/pyneng-examples-exercises/examples/17_serialization/json/sw_templates.json'
with open(test_file, 'r') as f:
    pisya = csv.reader(f)
    # print(list(pisya))
    for row in pisya:
        print(row)

# how to work with headers
with open(test_file, 'r')as f:
    pizda = csv.reader(f)
    header = next(pizda)
    print(f'HHHHHeaders{header}')
    for row in pizda:
        print(row)

# dictreader method
with open(test_file, 'r')as f:
    pizda = csv.DictReader(f)
    for row in pizda:
        print(row)

#######################################
# JSON
#######################################

with open(test_file_json) as f:
    pipi = json.load(f)
    print(type(pipi))
    print(pipi)


with open(test_file_json) as f:
    text = f.read()
    pipi = json.loads(text)
    print(type(pipi))
    print(pipi)

print('-----'*30)


vasya = {
  "access": [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable"
  ],
  "trunk": [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
  ]
}
# with open('test_json.json', 'w') as f:
#     f.write(json.dumps(vasya))
#
# with open('test_json.json', 'r') as f:
#     print(f.read())


with open('test_json.json', 'w') as f:
    json.dump(vasya, f, sort_keys=True, indent=2)

with open('test_json.json', 'r') as f:
    print(f.read())

print('-----'*30)
'''
Task 17.1
'''


def parse_sh_version(zalupa):
    regexp = re.findall(r'Cisco IOS Software, \d+ Software \S+, (?P<ios>Version \S+),'
                        r'.* uptime is (?P<uptime>\d* (?:days,)? \d* (?:hours,)? \d* (?:minutes)?)'
                        r'.* image file is (?P<image>\S+)', zalupa, re.DOTALL)
    return regexp


def write_inventory_to_csv(data_filenames, csv_filename):
    fata = headers
    for item in data_filenames:
        if os.path.exists(
                '/home/pashockys/progi_python/pyneng-examples-exercises/exercises_for_test/17_serialization/'+item):
            path = ('/home/pashockys/progi_python/pyneng-examples-exercises//exercises_for_test/17_serialization/'+item)
        else:
            path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/17_serialization/'+item
        with open(path, 'r')as f:
            fata.append(parse_sh_version(f.read()))
    print(fata)





headers = ['hostname', 'ios', 'image', 'uptime']
list_of_sh_version = ['sh_version_r1.txt', 'sh_version_r2.txt', 'sh_version_r3.txt']
write_inventory_to_csv(list_of_sh_version, 'ffff.out')
