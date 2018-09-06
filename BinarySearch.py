# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:29:12 2018

@author: Luis Palomino
"""

## Assumes the array is ordered

def binarySearch(x, n):
    if len(x) == 1:
        if x[0] == n:
            return True
        return False
    mid = len(x)//2
    if x[mid] == n:
        return True
    if n > x[mid]:
        return binarySearch(x[mid:len(x)], n)
    else:
        return binarySearch(x[0:mid], n)

lista = [1,2,3,4,5,6,7,8,9]
print(binarySearch(lista, 9))