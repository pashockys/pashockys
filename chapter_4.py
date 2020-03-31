
print(int('10', 2)) # something to int
print(bin(7)) #dec2bin
'''
1)переменные - это ссылки на разделы памятииии
2) То, что строки являются упорядоченным типом данных, позволяет обращаться к символам в
строке по номеру, начиная с нуля:
'''
string_1 = "pizda"
print(string_1[2], "--showing the third number, in this case it will be z")
print(string_1[-3], "--showing the third number, from the end, in this case it will be z")
print(string_1[2:3], "--showing numbers, from the second to third, in this case it will be z")
print(len(string_1), "--showing length of string")

string_2 = "\npizda\t"
print(string_2.strip(), "--cool method for avoiding spec symbols from the begining or from the end")
string_3 = "hui, zhopa, pizda"
print(string_3.split(), "-- splitting your string")
print(string_3.split("z"), "-- splitting your string with some symbol, that you choose")
string_4, string_5, string_6 = ["zalupa", "zzzzzzzzzzzalupa", "biba"]
print("{:15}{:15}{:>15}".format(string_4, string_5, string_6))  # trying to create a table with columns
print(f"asa:{string_4}")
print("asa:{}".format(string_4))
'''
LIST
'''
list_0 = ["hui", "zalupen'", "pizda"]
print(f"{list_0}")
list_1 = list(string_4)
print(f"{list_1}")
list_1[0] = "p"
print(f"{list_1}")
'''
Dictionary
'''
dict_0 = {
    'name': 'zalupa',
    'number': 13,
    'roflan': "Buldyga"
}
print(f"my new awesome dict:{dict_0}")
print(f"{dict_0['roflan']}")  # printing one element of dict
'''
Tuple
'''

tuple_1 = tuple('element')
print(tuple_1)

tuple_2 = 'element'
print(tuple_2)

tuple_3 = tuple(list_0)  # tuple from list
print(tuple_3)
'''
task 4.1
'''
nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
nat = nat.replace('FastEthernet', 'GigabitEthernet')
print(nat)
'''
task 4.2
'''
mac = 'AAAA:BBBB:CCCC'
mac = mac.replace(':', '.')
print(mac)
'''
task 4.3
'''
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
config_new = config.split()[-1].split(',')
print(config_new)

'''
task 4.4
'''
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans_new = sorted(list(set(vlans)))
print(vlans_new, vlans)
'''
task 4.5
'''
command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

command1_new = set(command1)
command2_new = set(command2)
print(f"first command{command1_new} vsds{command2_new}")

