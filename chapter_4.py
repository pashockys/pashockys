
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
command1_new = set(command1[command1.find('1')::])
command1_new.discard(',')
command2_new = set(command2[command2.find('1')::])
command2_new.discard(',')
command_intersection = sorted(list(command1_new & command2_new))
print(command_intersection)
'''
task 4.6
'''
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split()
print(ospf_route)
# Protocol:              OSPF
# Prefix:                10.0.24.0/24
# AD/Metric:             110/41
# Next-Hop:              10.0.13.3
# Last update:           3d18h
# Outbound Interface:    FastEthernet0/0
print(f"Protocol:        OSPF\nPrefix:{ospf_route[1]:>22}\nAD/Metric:{ospf_route[2][1:-1]:>13}\nNext-Hop:{ospf_route[4][:-1]:>17}\nLast update:{ospf_route[5][:-1]:>10}\nOutbound Interface:{ospf_route[6]:>10}")
'''
task 4.7
'''
mac = 'AAAA:BBBB:CCCC'
mac = mac.split(":")
bin_mac = ''
for i in range(len(mac)):
    bin_mac += str(bin(int(mac[i], 16)))
print(bin_mac.replace('0b', ''))
'''
task 4.8
'''
ip_template = '''
IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(192, 168, 3, 1))