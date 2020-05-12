#!/usr/bin/env python3
'''
Task 9.1
'''

# def access_port_generate(dict, template):
#     result = []
#     for i in dict.keys():
#         result.append('interface ' + i)
#         for item in template:
#             if 'vlan' in item:
#                 result.append(item + ' ' + str(dict[i]))
#             else:
#                 result.append(item)
#     return result
#
#
# access_mode_template = [
#     'switchport mode access', 'switchport access vlan',
#     'switchport nonegotiate', 'spanning-tree portfast',
#     'spanning-tree bpduguard enable'
# ]
# access_config = {
#     'FastEthernet0/12': 10,
#     'FastEthernet0/14': 11,
#     'FastEthernet0/16': 17
# }
#
# print(access_port_generate(access_config, access_mode_template))

'''
Task 9.2
'''

trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result = []
    for i in intf_vlan_mapping.keys():
        result.append('interface ' + i)
        for item in trunk_template:
            if 'allowed' in item:
                items = ''
                for value in intf_vlan_mapping[i]:
                    items = items + str(value) + ','
                    print(items)
                items = items[:-1]
                result.append(item + ' ' + items)
            else:
                result.append(item)
    return result


# print(generate_trunk_config(trunk_config, trunk_mode_template))

'''
Task 9.3
'''

def get_int_vlan_map(config_filename):
    try:
        path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/09_functions/'+config_filename
        open(path, 'r')
    except FileNotFoundError:
        print('It seems that you are not at home')
        path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/09_functions/'+config_filename
    with open(path, 'r') as f:
        result_dict = {}
        result_dict_trunk = {}
        for line in f:
            if 'interface' in line:
                interface = line.strip().split()[1]
                current_int = True
            if 'access vlan' in line:
                if current_int:
                    result_dict[interface] = int(line.strip().split()[-1])
                current_int = False
            if 'allowed vlan' in line:
                if current_int:
                    result_dict_trunk[interface] = [int(x) for x in line.strip().split()[-1].split(',')]
                current_int = False
    output = (result_dict_trunk, result_dict)
    return output

# print(get_int_vlan_map('config_sw1.txt'))

'''
Task 9.4
'''
ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)

def convert_config_to_dict(config_filename):
    try:
        path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/09_functions/' + config_filename
        open(path, 'r')
    except FileNotFoundError:
        print('It seems that you are not at home')
        path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/09_functions/' + config_filename
    with open(path, 'r') as f:
        dict_4 = {}
        main_line = ''
        for line in f:
            if not ignore_command(line, ignore) and '!' not in line:
                if line[0].isalpha():
                    main_line = line.strip()
                    dict_4[main_line] = []
                else:
                    dict_4[main_line].append(line.strip())
                    type(dict_4[main_line])
        return dict_4

# print(convert_config_to_dict('config_sw1.txt'))


