# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:15:56 2021

@author: User
"""

tup=(0,2,10,6)

def normalized(tup):
    tup_normal=()
    m=max(tup)
    for i in tup:
        tup_normal+=(i/m,)
    return tup_normal
    
print(normalized(tup))

