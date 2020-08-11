# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

prefix, ad_metr, _, n_hop, l_upd, o_int = ospf_route.replace(',', '').split()
print(f"Prefix              {prefix}\n"
      f"AD/Metric           {ad_metr.replace('[','').replace(']','')}\n"
      f"Next-Hop            {n_hop}\n"
      f"Last update         {l_upd}\n"
      f"Outbound Interface  {o_int}")
