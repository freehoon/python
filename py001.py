# -*- coding: utf-8 -*-
print("안녕 파이썬!")

a = 2000

print(a)

b = a + 3000  # type: int

print(b)

import math
print(math.pi)


c='''어서와
파이썬은
처음이지'''
print(c)

def plus_or_minus(arg):
    if arg < 0:
        return "minus"
    elif arg > 0:
        return "plus"

result = plus_or_minus(0)



a = (1,2,3)
b = (4,)
c = a + b
print(c)

gu = ['종로구','영등포구','덕양구']
gu[2] = '일산동구'
print(gu)

listNum = [1,2,3,4,5]
listNum[1:4] = 'x'
print(listNum)


import sys

print ("--sys.version--")
print (sys.version)

print ("\n--sys.version_info--")
print (sys.version_info)

print ("\n--sys.hexversion--")
print (sys.hexversion)


for path in sys.path:
    print(path)


