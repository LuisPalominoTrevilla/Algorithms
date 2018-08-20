# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:11:51 2018

@author: Luis Palomino
"""

"""
    Ejercicios de Tarea
"""

# Escribe una función que sume acumulativamente
def cumSum(n):
    if (n == 1):
        return 1;
    return n + cumSum(n-1)

# Sumar toos los digitos de un entero
def digitSum(number):
    # Check if number has only one digit
    if (number <= 9):
        return number
    return number % 10 + digitSum(number//10)

# Cambiar el orden de un string
def deReversa(string):
    if (len(string) == 1):
        return string
    return string[-1] + deReversa(string[:-1])

print(cumSum(3))
print(digitSum(43))
print(deReversa("raborper_a_yov"))