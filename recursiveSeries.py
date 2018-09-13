# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 23:58:20 2018

@author: Luis Palomino
"""

def recursive(n):
    if n == 1:
        return 1
    product = 1
    start = n*(n+1)//2 -n +1
    for i in range(start, start+n):
        product *= i
    return product + recursive(n-1)
    

print(recursive(4))