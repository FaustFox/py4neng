# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open("ospf.txt") as f:
    for line in f:
        _, prefix, metric, _, next_hop, last_upd, out_int = line.split()
        print(f'Prefix                  {prefix}\n'
              f'AD/Metric               {metric.strip("[").strip("]")}\n'
              f'Next-Hop                {next_hop.strip(",")}\n'
              f'Last Update             {last_upd.strip(",")}\n'
              f'Outbound Interface      {out_int}\n\n')

