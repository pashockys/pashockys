#!/usr/bin/env python3
import ipaddress
import subprocess
from tabulate import tabulate


def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def ping_ip_addresses(ip_list):
    new_list = [item for item in ip_list if check_ip(item)]
    success_ip = []
    denied_ip = []
    for ip in new_list:
        answer = subprocess.run(['ping', '-c', '2', '-W', '1', ip],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                encoding='utf-8')
        if answer.returncode == 0:
            print(answer.stdout)
            success_ip.append(ip)
        else:
            print(answer.stderr)
            denied_ip.append(ip)
    tuple(success_ip)
    return (success_ip, denied_ip)

def convert_ranges_to_ip_list(ip_list):
    output_list = []
    for item in ip_list:
        if '-' in item:
            convert_items = item.split('-')
            convert_octet_one = int(convert_items[0].split('.')[-1])
            convert_octet_two = int(convert_items[1].split('.')[-1])
            while convert_octet_one < convert_octet_two+1:
                output_list.append(convert_items[0][:-len(str(convert_octet_one))]+str(convert_octet_one))
                convert_octet_one += 1
            continue
        output_list.append(item)
    return output_list

def print_ip_table(accessible_ip, inaccessible_ip):
    sum_list = []
    header = ['Reachable', 'Unreachable']
    for i in range(max(len(accessible_ip), len(inaccessible_ip))):
        try:
            accessible_ip[i]
        except IndexError:
            sum_list.append(['', inaccessible_ip[i]])
            continue
        try:
            inaccessible_ip[i]
        except IndexError:
            sum_list.append([accessible_ip[i], ''])
            continue
        sum_list.append([accessible_ip[i], inaccessible_ip[i]])
    print(tabulate(sum_list, headers=header))


'''
Taks 12.1
'''
# if __name__ == '__main__':
#     list_of_ip = ['11.2.3.4', '1456.34.34.2', '12.2.2.2', '45.45.6.7', '8.8.8.8', '1.1.1.2']
#     print(ping_ip_addresses(list_of_ip))

'''
Taks 12.2
'''
# if __name__ == '__main__':
#     list_of_ip = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
#     print(convert_ranges_to_ip_list(list_of_ip))
'''
Taks 12.3
'''
if __name__ == '__main__':
    list_of_ip = ['8.8.4.4', '8.8.8.8', '1.1.1.1-3', '172.21.41.128-172.21.41.133']
    format_ip = ping_ip_addresses(convert_ranges_to_ip_list(list_of_ip))
    print_ip_table(format_ip[0], format_ip[1])