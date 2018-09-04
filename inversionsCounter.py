# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 07:42:48 2018

@author: Luis Palomino
"""
num = 0

def count(x):
    n = len(x)
    if(n == 1):
        return x
    # New array
    b = count(x[0:n//2])
    c = count(x[n//2:n])
    z = []
    global num
    num += countSplitInversions(b, c, z)
    return z

def countSplitInversions(b, c, z):
    i, j = 0, 0
    count = 0
    while i < len(b) and j < len(c):
        if c[j] < b[i]:
            count += len(b)-i
            z.append(c[j])
            j+=1
        else:
            z.append(b[i])
            i+=1
    while i < len(b):
        z.append(b[i])
        i+=1
    while j < len(c):
        z.append(c[j])
        j+=1
    return count
x=[]

integers = open("./integers.txt", "r")

for integer in integers:
    x.append(int(integer.rstrip()))
    
count(x)
print(num)

integers.close()