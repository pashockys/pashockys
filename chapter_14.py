#!/usr/bin/env python3
import re
int_line = 'MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'
vova_match = re.search('MTU', int_line)
print(vova_match)
print(vova_match.group())

'''
Допустим, необходимо написать регулярное выражение, которое описывает электронные ад-
реса в двух форматах: user@example.com и user.test@example.com. То есть, в левой части
адреса может быть или одно слово, или два слова, разделенные точкой.
'''
mail_1 = 'pashockys92@mail.ru'
mail_2 = 'pashockys.vova@yandex.ru'
def mail_all_match(ps):
    psi = re.search('\w+\.?\w*@\w+\.ru', ps)
    if psi:
        return psi.group()
    psi = re.search('[fF]ast', ps)
    if psi:
        return psi.group()
    return 'oops'
print(f'mail_1 {mail_all_match(mail_1)}\nmail_2 {mail_all_match(mail_2)}')


line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(f'puck {mail_all_match(line)}')

line = 'FastEthernet0/0 15.0.15.1 YES manual up up'
print(re.search('[^a-zA-Z]+', line).group())
print(re.search('fast|0/0', line).group())
# greedy off
print(re.search('(\d+\.)+?', line).group())
# regex groups
log2 = 'Oct→ 7fd63 12:49:15.941: %SW_MATM-4-MACFLAP_NOTIF: Host f04d.a206.7fd6' \
       'in vlan 1 is flapping between port Gi0/5 and port Gi0/16'
vova_match = re.search('Host (\w{4}\.\w{4}\.\w{1,4})in vlan (\d+).*port (\S+) and port (\S+)', log2)
print(f'simple print {vova_match.group(0)}')
print(f'output with proper numbers{vova_match.group(1, 2)}')
print(f'method {vova_match.groups()}')
