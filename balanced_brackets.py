# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 17:31:05 2022

@author: panna
"""

order = {"{":"}","(":")","[":"]"}
opener = []
closed = []



S  = "{}"
def balanced():
    opener = []
    closed = []
    if len(S)==1:
        return False
    for i in range(len(S)):
        if S[0] not in order:
            return False
        if S[i] in order:
            opener.append(S[i])
        elif S[i] == order[opener[-1]]:
                opener.pop(-1)
        else:
            closed.append(S[i])
    if len(opener)==0 and len(closed) == 0:
        return True
    else:
        return False
print(balanced())