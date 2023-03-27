#!/usr/bin/env python3

import sys

def my_printf(format_string, param):
    number = int(param)
    flag = False
    if number < 0:
        flag = True
        number *= -1
    param = str(number)[::-1]
    if flag:
        number = int(param)*-1
        param = str(number)

    print(format_string.replace('#g', str(int(param))))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[ i + 1].rstrip())
