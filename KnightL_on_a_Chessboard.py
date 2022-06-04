# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 21:38:53 2022

@author: panna
"""

import math
import os
import random
import re
import sys

# Complete the knightlOnAChessboard function below.
mem=[[]]
def adj(a, b, x, y, n):
    return filter(lambda v : v[0] >= 0 
      and v[1] >= 0 
      and v[0] < n 
      and v[1] < n,
      [
        [x + a, y + b],
        [x + a, y - b],
        [x - a, y + b],
        [x - a, y - b],
        [x + b, y + a],
        [x + b, y - a],
        [x - b, y + a],
        [x - b, y - a],
    ])
def mov(a,b,n):
    global mem
    if mem[a][b] is not None:
        return mem[a][b]
    visited = [[False] * n for _ in range(n)]    
    queue=[[0,0,0]]
    while len(queue)>0:
        x , y , l = queue.pop()
        if x == n-1 and y == n-1:
            mem[a][b]=l
            mem[b][a]=l
            return l
        neighbors=[
            [x_i,y_i]
            for x_i,y_i in adj(a,b,x,y,n) if visited[y_i][x_i]==False
        ]
        for x_i,y_i in neighbors:
            visited[y_i][x_i]=True
            queue.insert(0,[x_i,y_i,l+1])
    mem[a][b]=-1
    mem[b][a]=-1
    return -1    

def knightlOnAChessboard(n):
    global mem
    mem=[[None for _ in range(n+1)]for _ in range(n+1)]
    results=[]
    for a in range(1,n):
        results.append([])
        for b in range(1,n):
            results[a-1].append(mov(a,b,n))
    return results   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
