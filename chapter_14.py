#!/usr/bin/env python3
import re
import os
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
print(f'method groups{vova_match.groups()}')
# named groups
vova_match_named_group = re.search('Host (?P<mac>\w{4}\.\w{4}\.\w{1,4})in vlan (?P<vlan>\d+).*port (?P<int_1>\S+) '
                                   'and port (?P<int_2>\S+)', log2)
print(f'named_search_group {vova_match_named_group.group("mac")}')
print(f'method groupdict {vova_match_named_group.groupdict()}')
# repeat of detected result
bgp = '''
R9# sh ip bgp | be Network Network Next Hop 192.168.66.0/24 192.168.79.7
192.168.67.0/24 192.168.79.7 0 500 500 500 i 192.168.89.8 Metric LocPrf Weight Path 0 800 700 i 0
192.168.89.8 192.168.88.0/24 0 700 700 700 i 0 800 700 i 192.168.79.7 0 700 700 700 i 192.168.89.8 0 0 800 800 i
'''

def how_many_repeated_sequences(str_to_search):
    previous_end = 0
    end = len(str_to_search)
    out_list = []
    while True:
    # for i in range(0,4):
        bgp_search = re.search(r'(\d+) \1 \1', str_to_search[previous_end:end]) # \1 это как бы повторение первой группы. то есть типа макрос на первую группу
        try:
            out_list.append(bgp_search.group())
        except AttributeError:
            return out_list
        print(previous_end, bgp_search.end())
        if previous_end == bgp_search.end():
            return out_list
        else:
            previous_end = previous_end + bgp_search.end()
print(how_many_repeated_sequences(bgp))

'''
chapter_15
'''
# match groups default instead of typing 'none'
log2 = 'Oct→ 7fd63 12:49:15.941: %SW_MATM-4-MACFLAP_NOTIF: Host f04d.a206.7fd6' # we can find mac here
log3 = 'Oct→ 7fd63 12:49:15.941: %SW_MATM-4-MACFLAP_NOTIF:' # and cannot find here so we can use default value
vova_match_named_group = re.search('(?P<hui>\d+:\d+).* (?P<mac>\w+.\w+.\w+)?', log3)
print(vova_match_named_group.groups(default = 'hui')) # set default parameter if we cannot find anything

#mini-task

regex = (r'Device ID: (?P<device>\S+)|IP address: (?P<ip>\S+)|Platform: (?P<platform>\S+ [0-9a-zA-Z-]+)'
         r'|Cisco IOS Software, (?P<version>.* Version [0-9a-zA-Z-().]+)')
out_dict = {}
if os.path.exists('/home/pashockys/progi_python/pyneng-examples-exercises/examples/15_module_re/sh_cdp_neighbors_sw1.txt'):
    path = ('/home/pashockys/progi_python/pyneng-examples-exercises/examples/15_module_re/sh_cdp_neighbors_sw1.txt')
else:
    path = '/home/pashockys/Scripts/Natasha/pyneng-examples-exercises/examples/15_module_re/sh_cdp_neighbors_sw1.txt'
    print('It seems that you are not at home')
with open(path, 'r')as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            if match.lastgroup == 'device':
                device = match.group(match.lastgroup)
                out_dict[device] = {}
            else:
                out_dict[device][match.lastgroup] = match.group(match.lastgroup)
print(out_dict)

#find-iter
sh_ip_int_br = '''
...: R1#show ip interface brief
...: Interface IP-Address OK? Method Status Protocol
...: FastEthernet0/0 15.0.15.1 YES manual up up
...: FastEthernet0/1 10.0.12.1 YES manual up up
...: FastEthernet0/2 10.0.13.1 YES manual up up
...: FastEthernet0/3 unassigned YES unset up up
...: Loopback0 10.1.1.1 YES manual up up
...: Loopback100 100.0.0.1 YES manual up up
...: '''
result = re.finditer(r'(\S+) +([\d.]+) +\w+ +\w+ +(up|down|administratively down) +(up|down)', sh_ip_int_br)
for i in result:
    print(i.group(1))

#find-all
# result = re.findall(r'(\S+) +([\d.]+) +\w+ +\w+ +(up|down|administratively down) +(up|down)', sh_ip_int_br)
# result = re.findall(r'\w+\.\S+', sh_ip_int_br)
result = re.findall(r'(\w+\.)\S+', sh_ip_int_br)
print(result)

#compile
try_to_compile = re.compile(r'(\S+) +([\d.]+) +\w+ +\w+ +(up|down|administratively down) +(up|down)')
match = try_to_compile.search(sh_ip_int_br)
print(match.groups())

#flags .DOTALL
regex = (r'Device ID: (?P<device>\S+).*?IP address: (?P<ip>\S+).*?Platform: (?P<platform>\S+ [0-9a-zA-Z-]+)'
         r'.*?Cisco IOS Software, (?P<version>.*? Version [0-9a-zA-Z-().]+)')
with open(path, 'r')as f:
        match = re.findall(regex, f.read(), re.DOTALL)
        print(match)

#re.split
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
match = re.split('/', ospf_route)
print(match)
match2 = re.split('[\]\[/]', ospf_route)
print(match2)

#re.sub
match = re.sub('[\]\[/]', '-hui-', ospf_route)
print(match)