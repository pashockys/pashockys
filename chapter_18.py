#!/usr/bin/env python3
import os
import sqlite3
import re

# connection = sqlite3.connect('dhcp_snooping.db')
# cursor = connection.cursor()
# table creation
# cursor.execute('create table switch (mac text not null primary key, hostname text, model text, location text)')

# execute command

# data = [
# ('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
# ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
# ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
# ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]
# query = 'insert into switch values (?, ?, ?, ?)'
# for row in data:
#     cursor.execute(query, row)
# connection.commit()

# execute many command

# data2 = [
# ('0000.1111.0001', 'sw5', 'Cisco 3750', 'London, Green Str'),
# ('0000.1111.0002', 'sw6', 'Cisco 3750', 'London, Green Str'),
# ('0000.1111.0003', 'sw7', 'Cisco 3750', 'London, Green Str'),
# ('0000.1111.0004', 'sw8', 'Cisco 3750', 'London, Green Str')]
# query = "INSERT into switch values (?, ?, ?, ?)"
# cursor.executemany(query, data2)
# connection.commit()

# executescript command

# connection = sqlite3.connect('new_db.db')
# cursor = connection.cursor()
# cursor.executescript('''
# create table switches(hostname text not NULL primary key, location text);
# create table dhcp
# (mac text not NULL primary key, ip text, vlan text, interface text, switch text not null references switches(hostname));
# ''')

# fetchone command

# cursor.execute('select * from switch')
# print(cursor.fetchone())
# print('--**--'*30)
# # cycle with fetchone
# while True:
#     row = cursor.fetchone()
#     if row:
#         print(row)
#     else:
#         break
#
# # fetchmany command
#
# cursor.execute('select * from switch')
# print('--**--'*30)
# while True:
#     three_row = cursor.fetchmany(3)
#     if three_row:
#         print(three_row)
#     else:
#         break
#
# # fetchall command
#
# print('--**--'*30)
# cursor.execute('select * from switch')
# print(f'fetchall \n{cursor.fetchall()}')
#
# # print without fetch
#
# print('--**--'*30)
# print(f'without fetch')
# for i in cursor.execute('select * from switch'):
#     print(i)
#
# # print without fetch
#
# print('--**--'*30)
# print(f'without cursor')
# for i in connection.execute('select * from switch'):
#     print(i)
#
# # handling with exceptions
#
# try:
#     connection.execute("insert into switch values ('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str')")
# except sqlite3.IntegrityError as a:
#     print(f'why are you doing this\nerror: {a}')

'''
example
'''

# if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/examples/18_db/'):
#     dhcp_snoop = '/home/pashockys/progi_python/pyneng-examples-exercises/examples/18_db/dhcp_snooping.txt'
#     dhcp_schema = '/home/pashockys/progi_python/pyneng-examples-exercises/examples/18_db/dhcp_snooping_schema.sql'
# else:
#     dhcp_snoop = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/examples/18_db/dhcp_snooping.txt'
#     dhcp_schema = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/examples/18_db/dhcp_snooping_schema.sql'
# with open(dhcp_snoop, 'r') as f:
#     match = re.findall(r'(\S+) *(\S+) *\d+ *\S+ *(\S+) *(\S+)', f.read())
# if not os.path.exists('test.db'):
#     con = sqlite3.connect('test.db')
#     print('creating schema')
#     with open(dhcp_schema, 'r') as f:
#         con.executescript(f.read())
#     print('database was successfully created')
# else:
#     print('database already exists')
# try:
#     print('trying to fill database with some data')
#     con.executemany('insert into dhcp values (?, ?, ?, ?)', match)
# except sqlite3.IntegrityError as a:
#     print(f'why are you doing this\nerror: {a}')
# con.commit()
# con.close()

'''
task 18.3(creating_database)
'''

if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/exercises/18_db/task_18_5/'):
    path = '/home/pashockys/progi_python/pyneng-examples-exercises/exercises/18_db/task_18_5/'
else:
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/exercises/18_db/task_18_5/'
dhcp_schema = path+'dhcp_snooping_schema.sql'
dhcp_snoop = path+'dhcp_snooping.txt'

if os.path.exists('dhcp_snooping.db'):
    print('database already exists')
else:
    print('creating database................')
    con = sqlite3.connect('dhcp_snooping.db')
    with open(dhcp_schema, 'r') as f:
        con.executescript(f.read())
    con.commit()
    con.close()