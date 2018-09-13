# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:41:44 2018

@author: Luis Palomino
"""

import math

# Utilizando Newton Raphson para calcular la raiz de la ecuación:
# x^2 - n
# Donde:
# n -> es el valor del número cuya raiz cuadrada desea ser calculada
# x -> el valor aproximado de la raíz cuadrada

# Evaluar función f(x)
def f_x(x, n):
    return x*x - n

# Evaluar la derivada df/dx
def df_x(x):
    return 2*x

def raiz(x):
    # Tolerancia a calcular la raiz cuadrada
    tol = .001
    x0 = 1
    x1 = 1
    while math.fabs(f_x(x1, x)) >= tol:
        x1 = x0 - f_x(x0, x)/df_x(x0)
        x0 = x1
    return math.floor(x1)

print(raiz(190))