# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
user_pick = input('Выберите VLAN: ')
mac_table = []
with open('/home/alexk/pyneng/repos/pyneng23/exercises/07_files/CAM_table.txt') as f:
    for line in f:
        words = line.split()
        if words and words[0].isdigit() and words[0] == user_pick: 
            vlan, mac, _, interface = words # назначение str из list
            print(f"{vlan:<9}{mac:20}{interface}")
#            if vlan == user_pick:
#            mac_table.append([int(vlan), mac, interface]) # добавляем сроки в лист согласно порядку        
#for vlan, mac, interface in sorted(mac_table):
#    print(f"{vlan:<9}{mac:20}{interface}")