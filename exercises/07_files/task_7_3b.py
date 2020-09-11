# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('CAM_table.txt') as f_src:
    result = list()
    for line in f_src:
        line = line.split()
        if line and line[0].isdigit():
            result.append([int(line[0])] + line[1:])
    result.sort()

input_vlan = int(input('Enter VLAN: '))

for i in result:
    if input_vlan in i:
        i.remove('DYNAMIC')
        print(*i, sep='\t')

