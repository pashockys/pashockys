#!/usr/bin/env python3
import csv
import json
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

print('-----'*30)
with open('test_json.json', 'w') as f:
    json.dump(vasya, f, sort_keys=True, indent=2)

with open('test_json.json', 'r') as f:
    print(f.read())

