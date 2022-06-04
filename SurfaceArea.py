# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:06:56 2022

@author: panna
"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    
    shape = [len(A),len(A[0])]
    shape = (shape[0]*shape[1])
    front = 0
    back = 0
    Top = shape
    for i in A:
        front+=i[0]
        back+=i[-1]
        
    side1= sum(A[0])
    side2 = sum(A[-1])
    exposed_area_face = 0
    exposed_area_side = 0
    for i in A:
        for j in range(1,len(i)):
            exposed_area_side+=abs(i[j-1]-i[j])
            
    for i in range(1,len(A)):
        prev_row = A[i-1]
        row = A[i]
        for j in range(len(row)):
            exposed_area_face+=abs(row[j]-prev_row[j])
    return (exposed_area_face+exposed_area_side+front+back+Top*2+side1+side2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()