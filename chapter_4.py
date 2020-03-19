
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
