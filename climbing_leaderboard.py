# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:12:32 2022

@author: panna
"""

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    S=sorted(set(scores))
    S=S[::-1]
    """for i in scores:
        if i not in S:
            S.append(i)"""
    i=0
    j=len(S)-1
    rank=[]
    while i<len(alice):
        if alice[i]<S[j]:
            rank.append(j+2)
            i+=1
        elif alice[i]==S[j]:
            rank.append(j+1)
            i+=1
        else:
            if j>0:
                j-=1
            else:
                rank.append(1)
                i+=1
    return rank       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    alice_count = int(raw_input())

    alice = map(int, raw_input().rstrip().split())

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
