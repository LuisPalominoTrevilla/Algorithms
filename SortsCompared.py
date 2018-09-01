# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 23:02:46 2018

@author: Luis Palomino
"""

import time
import matplotlib.pyplot as plt
from random import randint

def bubbleSort(x):
    n = len(x)
    for i in range(n):
        for j in range (n-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                
def selectionSort(x):
    n= len(x)
    for i in range(n-1):
        min = i
        for j in range(i, n):
            if x[j] < x[min]:
                min = j
        x[i], x[min] = x[min], x[i]

def insertionSort(x):
    n = len(x)
    for i in range(n):
        k = i
        while k > 0 and x[k] < x[k-1]:
            x[k], x[k-1]= x[k-1], x[k]
            k-=1

def shellSort(x, h):
    while h>=1:
        for i in range(h,len(x)):
            aux = x[i]
            j=i-h
            while(j>=0 and aux<x[j]):
                x[j+h] = x[j]
                j=j-h
            x[j+h] = aux
        h=h-2

def BubbleSortGraph():
    for i in range(1,6):
        # llenar lista
        x = [randint(0, 100) for j in range(i*100)]
        start_time = time.time()
        # Sort list
        bubbleSort(x)
        elapsed_time = time.time() - start_time
        plt.scatter(i*100, elapsed_time)
    
    plt.show()

def SelectionSortGraph():
    for i in range(1,6):
        # llenar lista
        x = [randint(0, 100) for j in range(i*100)]
        start_time = time.time()
        # Sort list
        selectionSort(x)
        elapsed_time = time.time() - start_time
        plt.scatter(i*100, elapsed_time)
    
    plt.show()
    
def InsertionSortgraph():
    for i in range(1,6):
        # llenar lista
        x = [randint(0, 100) for j in range(i*100)]
        start_time = time.time()
        # Sort list
        insertionSort(x)
        elapsed_time = time.time() - start_time
        plt.scatter(i*100, elapsed_time)
    
    plt.show()

def ShellSortGraph():
    for i in range(1,6):
        # llenar lista
        x = [randint(0, 100) for j in range(i*100)]
        start_time = time.time()
        # Sort list
        # Consider h to be 45
        shellSort(x, 45)
        elapsed_time = time.time() - start_time
        plt.scatter(i*100, elapsed_time)
    
    plt.show()

print("Bubble Sort running time for n = 100, 200, 300, 400, 500")        
BubbleSortGraph()
print("Selection Sort running time for n = 100, 200, 300, 400, 500")
SelectionSortGraph()
print("Insertion Sort running time for n = 100, 200, 300, 400, 500")
InsertionSortgraph()
print("Shell Sort running time for n = 100, 200, 300, 400, 500")
ShellSortGraph()