#!/usr/bin/env python3
import re
import sys

def my_printf(format_string,param):
    if format_string == "" or param == "":
        print("")
        return
    znalazlem = re.search("#(\.\d+)?k", format_string)
    if not znalazlem:
        print(format_string)
        return
    zamiana = format_string[znalazlem.start():znalazlem.end()]
    length = len(param)
    if znalazlem.group(1):
        length = int(znalazlem.group(1)[1:])
    do_wypisania = format_string.replace(zamiana, param.swapcase()[:min(len(param),length)])
    print(do_wypisania)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
