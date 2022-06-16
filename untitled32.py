# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 08:53:25 2022

@author: panna
"""

sir = {'a':1,'b':2,'S':1}
l = [1,2,3]
print(list(enumerate(sir,1)))


print("Hello")

S = list(zip(l,sir))

S = [m for m in range(0,10)]
print(S)


def adder():
    i = 1
    while True:
        i+=1
        yield i

for num in adder():
    if num==10:
        break
    print(num)