#!/usr/bin/env python3

import sys
import re
def my_printf(format_string,param):
    if format_string == "" or param == "":
        print("")
        return

    znalazlem = re.search(r'#([1-9]\d*)?(\.\d+)?k', format_string)

    if not znalazlem:
        print(format_string)
        return
    replacement = znalazlem.group(0)
    zamiana = format_string[znalazlem.start():znalazlem.end()]
    param = param.swapcase()
    maxlen =  znalazlem.group(2)
    minlen = znalazlem.group(1)

    if maxlen:
        param = param[:int(maxlen[1:])]
    if minlen:
        param = " " * max(0, int(minlen) - len(param)) + param
    print(format_string.replace(replacement, param))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())

