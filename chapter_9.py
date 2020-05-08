#!/usr/bin/env python3

def access_port_generate(dict, template):
    result = []
    for i in dict.keys():
        result = template[0] + ' '+ str(dict[i])
        template.insert(0, 'interface ' + i)
        print(template)


access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

access_port_generate(access_config, access_mode_template)