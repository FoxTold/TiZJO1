#!/usr/bin/env python3

import sys
import re


def zamiana_litery(old_cyfra):
    return (old_cyfra * 9 + 1) % 10
def my_printf(format_string, param):
    match = re.search("#\.(\d+)g", format_string)
    if not match:
        print(format_string)
        return
    replacement , number = match.group(0) , int(match.group(1))
    param,absparam,zeros = int(param),abs(int(param)), max(0, number - len(str(abs(int(param)))))
    replace_with = (zeros * "0") + str(absparam)
    replace_with = ('-' if param < 0 else '') + ''.join([str(zamiana_litery(int(letter))) for letter in replace_with])
    print(format_string.replace(replacement, replace_with))

data = sys.stdin.readlines()
for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())