# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 09:12:57 2022

@author: panna
"""

S = [1,0,1,0,0,0,1,0]


k = 0
zeros = S.count(0)
while zeros:
    S[k] = 0
    zeros -= 1
    k+=1
for k in range(k,len(S)):
    S[k]=1
    


print(S)