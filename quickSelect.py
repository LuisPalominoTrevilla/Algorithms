# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:08:04 2018

@author: Luis Palomino
"""
from random import randint
def quickSelect(x, l, h, j):
    if j-1 < l or j-1 >= h or h-l < 1:
        return -1
    pivot = randint(l,h-1)
    x[l], x[pivot] = x[pivot], x[l]
    pivot_position = partition(x, l, h)
    if pivot_position+1==j:
        return x[pivot_position]
    elif pivot_position+1 > j:
        return quickSelect(x, l, pivot_position, j)
    else:
        return quickSelect(x, pivot_position+1, h, j)
def partition(x, l, h):
    p = x[l]
    i = l+1
    for j in range(l+1,h):
        if x[j] < p:
            x[i], x[j] = x[j], x[i]
            i+=1
    x[l], x[i-1] = x[i-1], x[l]
    return i-1
x=[7, 10, 4, 3, 20, 15]
print(quickSelect(x, 0, len(x), 7))