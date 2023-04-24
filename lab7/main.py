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

    param = int(param)
    param = hex(param)
    param = str(param)
    param = str(param.replace("0x",""))
    param = swap_letters(param)
    format_string = format_string.replace("#j",param)
    print(format_string)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
