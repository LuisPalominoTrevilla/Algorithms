# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 10:07:29 2018

@author: luis
"""

"""
    Best Case Scenario: O(n)
    Worst Case Scenario: Ω(n)
"""
def compara(lista, integer):
    for i in lista:
        if i == integer:
            return True
    return False

def method1():
    l = []
    for n in range(10000):
        l += [n]
    print(l)

def method2():
    l = []
    for n in range(10000):
        l.append(n)

def method3():
    l = [n for n in range(1000)]
    print(l)
    
def method4():
    l = list(range(1000))
    print(l)

# doctionaties

d = {'k1':2, 'k2':3, 'k4':5}

# get Item O(n)
print(d['k1'])

