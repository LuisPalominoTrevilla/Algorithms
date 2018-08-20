# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:43:58 2018

@author: Luis Palomino
"""
import math
import matplotlib.pyplot as plt
import time

# Reto 1
# Worst Case Time Complexity: O(2^n)
def numFibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return numFibonacci(n-1)+numFibonacci(n-2)

# Reto 2
# Worst Case Time Complexity: O(2^n)
def lastFibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return (lastFibonacci(n-1)+lastFibonacci(n-2))%10

# Reto 3
# Worst Case Time Complexity: O(nlog(n))
def mergeSort(numbers):
    mergeSortHelper(numbers, 0, len(numbers)-1)
def mergeSortHelper(numbers, low, high):
    def merge(A, B):
        C = [None]*(len(A)+len(B))
        i, j, k = 0, 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C[k] = A[i]
                i+=1
            else:
                C[k] = B[j]
                j+=1
            k+=1
        
        while i < len(A):
            C[k] = A[i]
            i+=1
            k+=1
        while j < len(B):
            C[k] = B[j]
            j+=1
            k+=1
            
        return C
    
    if high - low < 1:
        return
    mid = int((low+high)/2)
    mergeSortHelper(numbers, low, mid)
    mergeSortHelper(numbers, mid+1, high)
    C = merge(numbers[low:mid+1], numbers[mid+1:high+1])
    j=0
    for i in range(low, high+1):
        numbers[i] = C[j]
        j+=1

# Reto 1
def graph1():
    for i in range(0,15):
        # lista esta llena
        start_time = time.time()
        numFibonacci(i)
        elapsed_time = time.time() - start_time
        plt.scatter(i, elapsed_time)
    
    plt.show()
    
# Reto 2
def graph2():
    for i in range(0,15):
        # lista esta llena
        start_time = time.time()
        lastFibonacci(i)
        elapsed_time = time.time() - start_time
        plt.scatter(i, elapsed_time)
    
    plt.show()

# Reto 3
def graph3():
    for i in range(1,15):
        lista = []
        for x in range(i, -1, -1):
            lista.append(x)
        print(lista)
        print(" \n" )
        # lista esta llena
        start_time = time.time()
        mergeSort(lista)
        elapsed_time = time.time() - start_time
        plt.scatter(i, elapsed_time)
    
    plt.show()

# Reto 4
def graph4_1():
    for n in range(1,100):
        result = 6*n*math.log(n, 2)
        plt.scatter(n, result)
    
    plt.show()
    
def graph4_2():
    for n in range(1,100):
        result = 6*n
        plt.scatter(n, result)
    
    plt.show()

def graph4_3():
    for n in range(1,100):
        result = 6*n*math.log(n, 2)+ 6*n
        plt.scatter(n, result)
    
    plt.show()

def graph4_4():
    for n in range(1,100):
        result = n*math.log(n, 2)
        plt.scatter(n, result)
    
    plt.show()
