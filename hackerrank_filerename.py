# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:19:38 2022

@author: panna
"""
from itertools import combinations

newName = "ccc"
oldName = "cccc"

oldName = list(oldName)
to_delete = len(oldName)-len(newName)

i = 0
while i < (len(oldName)+4):
    oldName1 = oldName
    print(oldName1)
    for j in range(to_delete):
        oldName1.pop(j)
    #print(oldName1)
    oldName1 = None
    print(oldName1)
    i+=1
    print(i)