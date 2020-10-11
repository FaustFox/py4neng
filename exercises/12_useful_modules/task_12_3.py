# -*- coding: utf-8 -*-
"""
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
"""
from tabulate import tabulate


def print_ip_table(reachable_ip, unreachable_ip):
    ip_table = dict()

    ip_table['Reachable'] = reachable_ip
    ip_table['Unreachable'] = unreachable_ip

    print(tabulate(ip_table, headers='keys'))

    return None


if __name__ == '__main__':

    ip_r = ['10.1.1.1', '10.1.1.2']
    ip_u = ['10.1.1.7', '10.1.1.8', '10.1.1.9']

    print_ip_table(ip_r, ip_u)
