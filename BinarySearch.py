# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:29:12 2018

@author: Luis Palomino
"""

## Assumes the array is ordered

def binarySearch(x, n):
    if len(x) == 1:
        return x[0] == n
    mid = len(x)//2
    if x[mid] == n:
        return True
    if n > x[mid]:
        return binarySearch(x[mid:len(x)], n)
    else:
        return binarySearch(x[0:mid], n)

def bSearchIterative(x, num):
    low = 0
    high = len(x)-1
    
    while(True):
        mid = (low+high)//2
        if high < low:
            return False
        elif x[mid] == num:
            return (True, mid)
        elif x[mid] > num:
            high = mid-1
        else:
            low = mid+1
            

lista = [1,2,3,4,5,6,7,8,9]
print(bSearchIterative(lista, 1))