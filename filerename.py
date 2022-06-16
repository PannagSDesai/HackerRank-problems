# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:21:51 2022

@author: panna
"""

new = "aba"
old = "aba"
to_delete = len(old)-len(new)
#old1 = list(old)
#old1=old

if len(old) == len(new):
    same = old==new
    print(same)

for i in range(len(old)-to_delete+1):
    if i==0:
        print((old[to_delete:]))
    else:
        print((old[0:i]+old[i+to_delete:]))