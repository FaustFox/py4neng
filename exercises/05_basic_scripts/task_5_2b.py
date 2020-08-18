from sys import argv
# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#ip, mask = input("Enter network (IP/mask): ").split('/')
ip, mask = argv[1].split('/')
oct1, oct2, oct3, oct4 = ip.split('.')
bin_ip = f"{bin(int(oct1))[2:]:>08}\
{bin(int(oct2))[2:]:>08}\
{bin(int(oct3))[2:]:>08}\
{bin(int(oct4))[2:]:>08}"
bin_ip = f"{bin_ip[:int(mask)]:<032}"
bin_mask = f"{('1' * int(mask)):<032}"

print("Network:")
print(f"{int(bin_ip[:8], 2):<8} \
{int(bin_ip[8:16], 2):<8} \
{int(bin_ip[16:24], 2):<8} \
{int(bin_ip[24:], 2):<8}")
print(f"{bin_ip[:8]} {bin_ip[8:16]} {bin_ip[16:24]} {bin_ip[24:]}")
print()
print("Mask:")
print('/' + mask)
print(f"{int(bin_mask[:8], 2):<8} \
{int(bin_mask[8:16], 2):<8} \
{int(bin_mask[16:24], 2):<8} \
{int(bin_mask[24:], 2):<8}")
print(bin_mask[:8], bin_mask[8:16], bin_mask[16:24], bin_mask[24:])
