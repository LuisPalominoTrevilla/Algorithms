# -*- coding: utf-8 -*-

def multiplication(A, B):
    R = 0
    for i in range(0, B):
        R += A
    return R

def sumFormula(n):
    return n*(n+1)/2

def sumIterative(n):
    r = 0;
    for i in range(0, n+1):
        r+= i
    return r;

def sumRecursive(n):
    if n == 1:
        return 1
    return n + sumRecursive(n-1)
