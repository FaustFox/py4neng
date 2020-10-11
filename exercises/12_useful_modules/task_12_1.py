# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess


def ping_ip_addresses(source_addresses):

    ip_success = list()
    ip_fail = list()


    def ping_ip(ip, count=2):
        result = subprocess.run(f'ping -c {count} -n {ip}',
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                encoding='utf-8')

        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr


    for ip in source_addresses:
        flag, res = ping_ip(ip)
        if flag:
            ip_success.append(ip)
        else:
            ip_fail.append(ip)

    return ip_success, ip_fail


if __name__ == '__main__':
    print(ping_ip_addresses(['127.0.0.1', '8.8.8.8', '8.8.8']))

