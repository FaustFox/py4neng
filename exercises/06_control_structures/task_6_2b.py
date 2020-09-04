# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
check_int = False
check_dot = False
check_rng = False
ip_correct = False

while not ip_correct:
    ip_addr = input('Enter ip address: ')

    if ip_addr.count('.') == 3:
        oct1, oct2, oct3, oct4 = ip_addr.split('.')
        check_dot = True
        if oct1.isdigit() and oct2.isdigit() and oct3.isdigit() and oct4.isdigit():
            check_int = True
            if 0 <= int(oct1) < 256 \
               and 0 <= int(oct2) < 256 \
               and 0 <= int(oct3) < 256 \
               and 0 <= int(oct4) < 256:
                check_rng = True

    ip_correct = check_int and check_dot and check_rng

    if not ip_correct:
        print('Bad IP')


if 1 <= int(oct1) <= 223:
    print('unicast')
elif 224 <= int(oct1) <= 239:
    print('multicast')
elif ip_addr == '255.255.255.255':
    print('local broadcast')
elif ip_addr == '0.0.0.0':
    print('unassigned')
else:
    print('unused')

