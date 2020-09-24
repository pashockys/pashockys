#!/usr/bin/env python3
from netmiko import ConnectHandler
'''
task 6.1
'''

device_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.11',
    'username': 'admin',
    'password': 'password',
    'secret': 'password'
}


def netmiko_ssh(**params_dict):
    ssh = ConnectHandler(**params_dict)
    ssh.enable()
    def send_show_command(command):
        if command == 'close':
            print('connection wad closed')
            return ssh.disconnect()
        try:
            result = ssh.send_command(command)
        except AttributeError:
            print('session was closed')
            return False
        return result
    return send_show_command


# if __name__ == "__main__":
#     r1 = netmiko_ssh(**device_params)
#     print(r1('sh clock'))
#     print(r1('close'))
#     print(r1('sh ip int br'))

'''
task 6.2
'''

def count_total():
    sum1 = 0
    def inner(num):
        nonlocal sum1
        sum1 = num + sum1
        print(f'sum {sum1}')
    return inner

# count = count_total()
# count(10)
# count(20)
# count(30)

'''
task 6.2a
'''



def count_total():
    sum1 = 0
    def inner():
        def summ(num):
            nonlocal sum1
            sum1 = num + sum1
            print(f'sum {sum1}')
        inner.buy = summ
    return inner

# count = count_total()
# count()
# count.buy(10)
# count.buy(20)
# count.buy(30)

'''
task 6.3
'''

def listing():
    list_res = []
    def inner_f():
        def add_to_queue(var):
            list_res.append(var)
            print(f'you have just added item {var} to queue '
                  f'now the whole queue looks like this: '
                  f'{list_res}')
        def del_from_queue(var):
            try:
                list_res.remove(var)
                print(f'you have just removed item {var} from queue '
                      f'now the whole queue looks like this: '
                      f'{list_res}')
            except ValueError:
                print(f" you are trying to remove {var} "
                      f"but we don't have this item in our list")
        inner_f.put = add_to_queue
        inner_f.get = del_from_queue
    return inner_f

nikita = listing()
nikita()
nikita.put(20)
nikita.get(20)
nikita.get(30)
nikita.put('sds')
