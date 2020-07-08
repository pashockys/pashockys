#!/usr/bin/env python3
import sqlite3
import sys
query = "select * from dhcp where {}={} and active={}"
query_all = "select * from dhcp where active={}"
con = sqlite3.connect('dhcp_snooping.db')


# def eject_some_data_from_table():
#     if len(sys.argv) == 3:
#         try:
#             key, value = sys.argv[1:]
#             print('')
#             result = con.execute(query.format(key, value))
#         except sqlite3.OperationalError:
#             result = None
#             print('try the right query')
#     elif len(sys.argv) == 1:
#         result = con.execute(query_all)
#     else:
#         result = None
#         print('u can type two or zero variables')
#     return result

def eject_some_data_from_table():
    result = []
    if len(sys.argv) == 3:
        try:
            key, value = sys.argv[1:]
            result.append(con.execute(query.format(key, value, 1)))
            result.append(con.execute(query.format(key, value, 0)))
        except sqlite3.OperationalError:
            result = None
            print('try the right query')
    elif len(sys.argv) == 1:
        result.append(con.execute(query_all.format(1)))
        result.append(con.execute(query_all.format(0)))
    else:
        result = None
        print('u can type two or zero variables')
    return result


def printing_values(data):
    print('active connections:')
    print('{:19} {:15} {:6} {:18} {:6} {:3}'.format('mac', 'ip', 'vlan', 'int', 'switch', 'active'))
    for i in data[0]:
        print('{:19} {:15} {:6} {:18} {:6} {:3}'.format(*i))
    print('non-active connections:')
    print('{:19} {:15} {:6} {:18} {:6} {:3}'.format('mac', 'ip', 'vlan', 'int', 'switch', 'active'))
    for i in data[1]:
        print('{:19} {:15} {:6} {:18} {:6} {:3}'.format(*i))



poo = eject_some_data_from_table()
if poo:
    printing_values(poo)
else:
    print('Nothing to show')

