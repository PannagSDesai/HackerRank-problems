# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 17:46:00 2022

@author: panna
"""
import re

S="255.120.0.0"

def valid_ip(S):

    if len(re.findall(r'(\.?\b[0-255]{1,3}\b\.?)',S)) == 4:
           return("valid")
    
    else:
        return("invalid")
    
    
print(valid_ip(S))