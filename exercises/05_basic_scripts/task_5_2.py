# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip, mask = input("Enter network (IP/mask): ").split('/')
ip = ip.split('.')
mask =f"{('1' * int(mask)):<032}"

print("Network:")
print(f"{int(ip[0]):<8} {int(ip[1]):<8} {int(ip[2]):<8} {int(ip[3]):<8}")
print(f"{int(ip[0]):>08b} {int(ip[1]):>08b} {int(ip[2]):>08b} {int(ip[3]):>08b}")
print()
print("Mask:")
print('/' + str(mask.count('1')))
print(f"{int(mask[:8], 2):<8} {int(mask[8:16], 2):<8} {int(mask[16:24], 2):<8} \
{int(mask[24:], 2):<8}")
print(mask[:8], mask[8:16], mask[16:24], mask[24:])
