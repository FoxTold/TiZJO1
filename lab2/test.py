#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.' and format_string[idx+3]=='k':
                length = int(format_string[2])
                print(param.swapcase()[:length],end="")
                shouldDo=False
            else:
                print(format_string[idx-3],end="")
        else:
            shouldDo=True
    print("")

my_printf("#.2k","asd")
