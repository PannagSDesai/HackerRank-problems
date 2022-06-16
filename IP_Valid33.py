# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 17:46:00 2022

@author: panna
"""
import re

S="255.12.0.14"


reg = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

"""def valid_ip(S):
    print(re.findall(r'([0-255].[0-255].[0-255].[0-255]\.)',S))
    if len(re.findall(r'(\.?\b[0-255]{1,3}\b\.?)',S)) == 4:
           return("valid")
    
    else:
        return("invalid")
    
    
print(valid_ip(S))"""

reg = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'

print(re.search(reg,S))