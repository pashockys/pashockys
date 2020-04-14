#!/usr/bin/env python3
'''
task 7.1
'''

routing_template = '''
Protocol:           
{0}
Prefix:             {1}               
AD/Metric:          {2}
Next-Hop:           {3}
Last update:        {4}
Outbound Interface: {5}'''
with open('/home/pashockys/progi_python/pyneng-examples-exercises/exercises/07_files/ospf.txt', 'r') as f:
    # for line in f:
    #     print(line.strip())
    # print(f.read())
    formatted_data = f.readline().split()
    if formatted_data[0] == 'O':
        formatted_data[0] = 'OSPF'
    for element in formatted_data:
        if element.endswith(','):
            formatted_data[formatted_data.index(element)] = element[:-1]
    print(routing_template.format(formatted_data[0],
                                  formatted_data[1],
                                  formatted_data[2],
                                  formatted_data[4],
                                  formatted_data[5],
                                  formatted_data[6]))

    # print(f.readlines())



