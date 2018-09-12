# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:41:44 2018

@author: Luis Palomino
"""

import math

def f_x(n, x):
    return n**2 - x

def df_x(n):
    return 2*n

def sqrt(x):
    tol = .001
    x0 = 1
    x1 = 1
    while math.fabs(f_x(x1, x)) >= tol:
        x1 = x0 - f_x(x0, x)/df_x(x0)
        x0 = x1
    return math.floor(x1)

print(sqrt(25))