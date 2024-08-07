# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv

def get_int_vlan_map(config_filename):
    """
    Функция обрабатывает конфиг коммутатора и создает кортеж с двумя словарями,
    для access и для trunk
    """

    with open(config_filename) as f:
        access = {}
        trunk = {}
        for row in f:
            if row.startswith('interface '):
                intf = row.split()[-1]
            elif 'access vlan' in row:
                access.update({intf: int(row.split()[-1])})
            elif 'access' in row:
                access[intf] = 1
            elif 'trunk allowed' in row:
                trunk[intf] = [int(v) for v in row.split()[-1].split(',')]
    return access, trunk


print(get_int_vlan_map('/home/alexk/pyneng/repos/pyneng23/exercises/09_functions/config_sw2.txt'))