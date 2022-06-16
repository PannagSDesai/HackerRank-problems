# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 18:20:04 2022

@author: panna
"""

from itertools import combinations

S =  [12, 3, 4, 1, 6, 9]
s = 24

for i in combinations(S,3):
    if sum(i) == s:
        print(i)