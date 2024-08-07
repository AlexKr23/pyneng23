# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from sys import argv

def get_int_vlan_map(config_filename):
    """
    Функция обрабатывает конфиг коммутатора и создате кортеж с двумя словарями,
    для access и для trunk
    """
    output = tuple()
    with open(config_filename) as f:
        temp = []
        access = {}
        trunk = {}
        for row in f:
            if row.startswith('interface F') or 'access vlan' in row or 'trunk allowed' in row:
                temp.append(row.rstrip())
        for i in range(0, len(temp), 2):
            if i + 1 == len(temp):
                break
            elif 'access' in temp[i + 1]:
                access[temp[i].split()[-1]] = int(temp[i + 1].split()[-1])
            elif 'trunk' in temp[i + 1]:
                trunk[temp[i].split()[-1]] = [int(x) for x in temp[i + 1].split()[-1].split(',')]
        output = (access, trunk)    
    return output


print(get_int_vlan_map('/home/alexk/pyneng/repos/pyneng23/exercises/09_functions/config_sw1.txt'))