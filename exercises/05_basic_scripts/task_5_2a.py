# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28  в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#ip, mask = input("Enter network (IP/mask): ").split('/')
ip, mask = "10.0.1.1/24".split('/')
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
