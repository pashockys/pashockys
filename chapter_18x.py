import sqlite3
import sys
key, value = sys.argv[1:]
print(key, value)
query = f'select * from dhcp where {key} = ?'
con = sqlite3.connect('test.db')
result = con.execute(query, (value, ))
for i in result:
    print(i)
con.close()
