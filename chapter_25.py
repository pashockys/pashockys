#!/usr/bin/env python3
def transform_topology(new_dict):
    repeated_dict = {}
    for key, value in new_dict.items():
        for key2, value2 in new_dict.items():
            if key == value2 and value == key2:
                if key2 == repeated_dict.get(value2):
                    continue
                else:
                    repeated_dict[key2] = value2
    result = {k: v for k, v in new_dict.items() if k not in repeated_dict}
    return result
topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
class Topology:
    def __init__(self, new_dict):
        repeated_dict = {}
        for key, value in new_dict.items():
            for key2, value2 in new_dict.items():
                if key == value2 and value == key2:
                    if key2 == repeated_dict.get(value2):
                        continue
                    else:
                        repeated_dict[key2] = value2
        result = {k: v for k, v in new_dict.items() if k not in repeated_dict}
        self.topology = result


top = Topology(topology_example)
print(top.topology)













def transform_topology(filename):
    with open(filename, 'r') as f:
        temp_file = yaml.safe_load(f)
    new_dict = {}
    repeated_dict = {}
    for keys_out in temp_file.keys():
        for keys_in in temp_file[keys_out].keys():
            for keys, item in temp_file[keys_out][keys_in].items():
                new_dict[(keys_out, keys_in)] = (keys, item)
    for key, value in new_dict.items():
        for key2, value2 in new_dict.items():
            if key == value2 and value == key2:
                if key2 == repeated_dict.get(value2):
                    continue
                else:
                    repeated_dict[key2] = value2
    draw_topology(repeated_dict, 'hhhhhhh')
    return repeated_dict