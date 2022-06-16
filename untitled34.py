# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 10:19:56 2022

@author: panna
"""
 
s="abc  "
def check_palindrome(s):
    l = len(s)
    i = 0
    j = l-1

    while i <= j:
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True
    
if __name__ == "__main__":
    
    
    #print(s)
    count = 0
    flag = 0
    while (len(s)>0):
        if(check_palindrome(s)):
            flag = 1
            break
        else:
            count += 1
            
            s = s[:-1]
    print(count)