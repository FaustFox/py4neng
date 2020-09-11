# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]

with open(argv[1]) as f_src, open('config_sw1_cleared.txt', 'w') as f_dst:
    for line in f_src:
        for item in ignore:
            if item in line:
                break
        else:
            f_dst.write(line)

