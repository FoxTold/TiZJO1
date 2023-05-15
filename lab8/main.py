#!/usr/bin/env python3
import re
import sys

def swap_letters(word):
    result = ""
    for i in word:
        if i == 'a':
            result+='g'
        elif i == 'b':
            result+= 'h'
        elif i == 'c':
            result +='i'
        elif i == 'd':
            result += 'j'
        elif i == 'e':
            result +='k'
        elif i == 'f':
            result +='l'
        else:
            result += i
    return result
def my_printf(format_string,param):
    match = re.search("#\.(\d+)j", format_string)
    if not match:
        print(format_string)
        return

    replace = match.group(0)
    min_length = match.group(1)

    replace_with = str(hex(int(param)))
    replace_with = replace_with.replace('0x', '')
    replace_with = max(0, len(replace_with) - int(min_length)) * "0" + replace_with

    replace_with = swap_letters(replace_with)

    print(format_string.replace(replace, replace_with))
    print(format_string)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
