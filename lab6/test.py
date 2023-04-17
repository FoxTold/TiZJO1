import sys
import re

def my_printf(format_string,param):
    if format_string == "":
        print("")
        return
    znalazlem = re.search("#(\.\d+)?k", format_string)
    if not znalazlem:
        print(format_string)
        return
    zmiana = ""
    for cyfra in param:
        zmiana += str((int(cyfra)*9+1)%10)
    zamiana = format_string[znalazlem.start():znalazlem.end()]
    length = len(param)
    if znalazlem.group(1):
        length = int(znalazlem.group(1)[1:])
    print(format_string.replace(zamiana, param.swapcase()[:min(len(param),length)]))

my_printf("## kk# []][[[] #-------k #--k #-2.k #.-2k,,...,,.","asd")
