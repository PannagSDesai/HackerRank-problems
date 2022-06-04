# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:09:54 2022

@author: panna
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = str(s.replace(" ",""))
    string_len = len(s)
    up_lim = math.ceil(math.sqrt(string_len))
    low_lim = math.floor(math.sqrt(string_len))
    indx_in_string = 0
    holder = []
    
    if up_lim * low_lim < len(s):
        low_lim = up_lim
        
    for row in range(low_lim):
        holder.append(s[indx_in_string:indx_in_string + up_lim])
        indx_in_string += up_lim
        
    holder_1 = []
    
    for j in range(up_lim):
        string_holder = ""
        for i in holder:
            try:
                string_holder = string_holder + i[j]
            except:
                pass
            #print(string_holder)
        holder_1.append(string_holder)
        
    string_final = ""
    for i in holder_1:
        string_final = string_final + i
        string_final = string_final + " "
        
    return (string_final)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
