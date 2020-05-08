#!/usr/bin/env python3

def access_port_generate(dict, template):
    result = []
    for i in dict.keys():
        result.append('interface ' + i)
        for item in template:
            if 'vlan' in item:
                result.append(item + ' ' + str(dict[i]))
            else:
                result.append(item)
    return result


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

print(access_port_generate(access_config, access_mode_template))