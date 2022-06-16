# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:30:27 2022

@author: panna
"""

D = 0.000111111111111
arr = [1,1,0,-1,-1,1]



A = [[1,2,3],[4,5,6],[7,8,9]]

def diagonalDifference(arr):
    # Write your code here
    s = []
    p = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i==j:
                p.append(arr[i][i])
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == len(arr[i])-j-1:
                s.append(arr[i][j])
                
    return(sum(s))

print(diagonalDifference(A))

for i in range(len(A)):
    for j in range(len(A[i])):
        if i+j == len(A[i])-1:
            print(A[i][j])