# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 21:34:54 2022

@author: panna
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    grid_t = []
    for i in range(n):
        s =[]
        for j in grid[i]:
            s.append(j)
        grid_t.append(s)

    for i in range(1, len(grid) - 1):
        grid[i] = list(grid[i])

    for i in range(1,n-1):
        for j in range(1,n-1):
            if int(grid_t[i][j]) > max(int(grid_t[i-1][j]),int(grid_t[i][j-1]),int(grid_t[i+1][j]),int(grid_t[i][j+1])):
                    grid[i][j] = 'X'
    for i in range(1,len(grid)-1):
        grid[i] = ("").join(grid[i])
            
    return(grid)
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
