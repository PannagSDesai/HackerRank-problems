# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 21:33:23 2022

@author: panna
"""

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    rem=3
    while t>rem:
        t-=rem
        rem*=2
    return rem-t+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
