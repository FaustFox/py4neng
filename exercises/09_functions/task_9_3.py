# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    trunk_config = dict()
    access_config = dict()
    T_KEYWORD = 'allowed vlan '
    A_KEYWORD = 'access vlan '

    with open(config_filename) as f:
        for line in f:
            if 'interface' in line:
                key  = line.split()[1]
                continue
            if T_KEYWORD in line:
                value = line[line.index(T_KEYWORD) +
                                 13:].rstrip().split(',')
                f_value = list(map(int, value))
                trunk_config[key] = f_value
            elif A_KEYWORD in line:
                value = int(line[line.index(A_KEYWORD) + 12:].rstrip())
                access_config[key] = value

    return access_config, trunk_config

print(get_int_vlan_map('config_sw1.txt'))

