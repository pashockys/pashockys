#!/usr/bin/env python3


topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

topology_example2 = {('R11', 'Eth0/0'): ('SW12', 'Eth0/1'),
                    ('R21', 'Eth0/0'): ('SW12', 'Eth0/2'),
                    ('SW11', 'Eth0/3'): ('R32', 'Eth0/0')}


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, new_dict):
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
        return result

    def __add__(self, other):
        sum = {}
        sum.update(self.topology)
        sum.update(other.topology)
        return Topology(sum)


top = Topology(topology_example)
top2 = Topology(topology_example2)
print(f'at first\n{top.topology}\nand\n{top2.topology}')
top3 = top + top2
print(f"zalupa\n{top3.topology}")
print(f'then\n{top.topology}\nand\n{top2.topology}')

