# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 21:36:21 2022

@author: panna
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    count=0
    i=0
    x=sorted(x)
    while i<len(x):
        t=x[i]
        while i<len(x) and x[i]-t<=k:
            i+=1
        count+=1
        t=x[i-1]
        while i<len(x) and x[i]-t<=k:
            i+=1
    return count            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
