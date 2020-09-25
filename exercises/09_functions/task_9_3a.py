# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            elif 'mode access' in line:
                access_config[key] = 1

    return access_config, trunk_config

print(get_int_vlan_map('config_sw1.txt'))

