
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
