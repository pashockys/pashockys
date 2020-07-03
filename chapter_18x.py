#!/usr/bin/env python3
import sqlite3
import sys

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


key, value = sys.argv[1:]
query_dict = {
    'vlan': 'select mac, ip, interface from dhcp where vlan = ?',
    'mac': 'select vlan, ip, interface from dhcp where mac = ?',
    'ip': 'select vlan, mac, interface from dhcp where ip = ?',
    'interface': 'select vlan, mac, ip from dhcp where interface = ?'
}
keys = query_dict.keys()
if not key in keys:
    print('Enter key from {}'.format(', '.join(keys)))
else:
    con = sqlite3.connect('test.db')
    con.row_factory = sqlite3.Row
    query = query_dict[key]
    result = con.execute(query, (value,))
    print('\nDetailed information for host(s) with', key, value)
    for row in result:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
        print('-' * 40)
