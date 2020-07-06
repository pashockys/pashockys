#!/usr/bin/env python3
import sqlite3
import sys
import os
import yaml
import re
from datetime import timedelta, datetime

# key, value = sys.argv[1:]
# query = f'select * from dhcp where {key} = ?'
# con = sqlite3.connect('test.db')
# result = con.execute(query, (value, ))
# for i in result:
#     print(i)
# con.close()

# key, value = sys.argv[1:]
# keys = ['mac', 'ip', 'vlan', 'interface']
# keys.remove(key)
# query = 'select * from dhcp where {} = ?'.format(key)
# con = sqlite3.connect('test.db')
# # следующая команда деает так, что теперь к result можно будет обращаться по имени. и result теперь будет возвращать
# # не кортеж, как если бы этой команды не было, а <sqlite3.Row object at 0x7f85421cc2b0>
# con.row_factory = sqlite3.Row
# result = con.execute(query, (value, ))
# print('\nDetailed information for host(s) with', key, value)
# for row in result:
#     for k in keys:
#         print('{:12}: {}'.format(k, row[k]))
#     print('-' * 40)


# key, value = sys.argv[1:]
# query_dict = {
#     'vlan': 'select mac, ip, interface from dhcp where vlan = ?',
#     'mac': 'select vlan, ip, interface from dhcp where mac = ?',
#     'ip': 'select vlan, mac, interface from dhcp where ip = ?',
#     'interface': 'select vlan, mac, ip from dhcp where interface = ?'
# }
# keys = query_dict.keys()
# if not key in keys:
#     print('Enter key from {}'.format(', '.join(keys)))
# else:
#     con = sqlite3.connect('test.db')
#     con.row_factory = sqlite3.Row
#     query = query_dict[key]
#     result = con.execute(query, (value,))
#     print('\nDetailed information for host(s) with', key, value)
#     for row in result:
#         for k in row.keys():
#             print('{:12}: {}'.format(k, row[k]))
#         print('-' * 40)

'''
task 18.3(add_data)
'''

if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/exercises/18_db/task_18_5/'):
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/18_db/task_18_5/'
    new_path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/18_db/task_18_5/new_data/'
else:
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/18_db/task_18_5/'
    new_path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/18_db/task_18_5/new_data/'
query_sw = 'insert into switches values (?, ?)'
query_dhcp = 'replace into dhcp values (?, ?, ?, ?, ?, 1, datetime("now"))'
con = sqlite3.connect('dhcp_snooping.db')


def get_data_from_files(path):
    '''
    :param path: expecting folder with some files that contains data
    :return: list of list of tuples with data
    '''
    data_dhcp = []
    regex = re.compile(r'(\S+) *(\S+) *\d+ *\S+ *(\S+) *(\S+)')
    for name_of_file in os.listdir(path):
        if 'dhcp_snooping.txt' in name_of_file:
            switch_name = re.search(r'^(\S+?)_', os.path.basename(name_of_file))
            with open(path+name_of_file, 'r') as f:
                for line in f.readlines():
                    match = regex.search(line)
                    if match:
                        out = match.groups()+(switch_name.group(1), )
                        data_dhcp.append(out)
        if 'switches.yml' in name_of_file:
            with open(path+name_of_file, 'r') as f:
                data_switches = yaml.safe_load(f)
            data_sw = []
            for string, string_1 in data_switches['switches'].items():
                data_sw.append((string, string_1))
    return data_dhcp, data_sw


def writing_to_table(table_name, data, query):
    if table_name == 'dhcp':
        con.execute(f"update {table_name} set active = 0 where active = 1")
    print(f'trying to write some data in {table_name} table')
    for string in data:
        try:
            con.execute(query, string)
        except sqlite3.IntegrityError:
            print(f'INFO: this data has already been inserted{string}')
    con.commit()


def delete_old_data(table_name):
    now = datetime.today().replace(microsecond=0)
    week_ago = now - timedelta(days=7)
    con.execute(f"delete from {table_name} where last_active < '{week_ago}'")
    con.commit()


# data = get_data_from_files(path)
# writing_to_table(table_name='dhcp', data=data[0], query=query_dhcp)
# writing_to_table(table_name='switches', data=data[1], query=query_sw)
delete_old_data(table_name='dhcp')
# con.close()




