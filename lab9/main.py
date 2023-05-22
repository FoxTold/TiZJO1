#!/usr/bin/env python3
import re
import sys

def swap_decimal(word):
    result = ""
    for i in word:
        if i == '0':
            result+='a'
        elif i == '1':
            result+= 'b'
        elif i == '2':
            result +='c'
        elif i == '3':
            result += 'd'
        elif i == '4':
            result +='e'
        elif i == '5':
            result +='f'
        elif i=='6':
            result+='g'
        elif i=='7':
            result+='h'
        elif i=='8':
            result+='i'
        elif i=='9':
            result+='j'
    return result

def swap_fractal(word):
    result = ""
    for i in word:
        num = int(i)
        new_num = (num+5)%10
        result+= str(new_num)
    return result
def my_printf(format_string,param):
    match = re.search("#\.(\d+)h", format_string)
    if not match:
        print(format_string)
        return

    replace = match.group(0)
    min_length = int(match.group(1))

    num = param.split(".")
    if len(num) == 2:
        decimal = swap_decimal(num[0])
        fractal = swap_fractal(num[1])
        
    if min_length>len(fractal):
        fractal = fractal + ("0"*(min_length-len(fractal)))
    elif min_length<len(fractal):
        fractal =  fractal[:len(fractal)-min_length]

    replace_with = decimal + "." + fractal

    print(format_string.replace(replace, replace_with))


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
