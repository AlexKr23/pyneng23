# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ospf_list = []
with open('/home/alexk/pyneng/repos/pyneng23/exercises/07_files/ospf.txt') as osfp:
    for line in osfp:
        ospf_list.append(line.replace(",", " ").replace("[", "").replace("]", "").split())

output = "\n{:25} {}" * 5
for row in ospf_list:   
    print(output.format(
            "Prefix", row[1],
            "AD/Metric", row[2],
            "Next-Hop", row[4],
            "Last update", row[5],
            "Outbound Interface", row[6],
    ))
