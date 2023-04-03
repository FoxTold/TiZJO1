#!/usr/bin/env python3

import sys
import re
def my_printf(format_string,param):
    if format_string == "":
        print("")
        return

    znalazlem = re.search(r'#([1-9]\d*)?g', format_string)

    if not znalazlem:
        print(format_string)
        return
    result = ""
    isNegative = False
    if int(param) < 0:
        param = str(int(param)*-1)
        isNegative = True
    for a in param:
        letter = int(a)-1
        if letter < 0:
            letter = "9"
        result += str(letter)
    param = result
    replacement = znalazlem.group(0)
    minlen = znalazlem.group(1)
    if isNegative:
        param = "-" + param
    if minlen:
        param = " " * max(0, int(minlen) - len(param)) + param
    print(format_string.replace(replacement, param))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())




