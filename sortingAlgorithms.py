import random
from queue import Queue

# Bubble Sort algorithm -> Worst Case Time Complexity: O(n^2)
def bubbleSort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range (n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# Insertion Sort algorithm -> Worst Case Time Complexity: O(n^2)
def insertionSort(numbers):
    n = len(numbers)
    for i in range(n):
        k = i
        while k > 0 and numbers[k] < numbers[k-1]:
            numbers[k], numbers[k-1]= numbers[k-1], numbers[k]
            k-=1

# Selection Sort algorithm -> Worst Case Time Complexity: O(n^2)
def selectionSort(numbers):
    n= len(numbers)
    for i in range(n-1):
        min = i
        for j in range(i, n):
            if numbers[j] < numbers[min]:
                min = j
        numbers[i], numbers[min] = numbers[min], numbers[i]

# Quicksort algorithm -> Worst Case Time Complexity: O(n^2)
# But tends to behave as a O(nlog(n))
def quickSort(numbers):
    quickSortHelper(numbers, 0, len(numbers)-1)
def quickSortHelper(numbers, low, high):
    # helper function that partitions an array into two depending on the pivot
    def partition(numbers, low, high):
        C = [None]*len(numbers)
        pivot = high
        i, j = low, high
        for x in range(low, high):
            if numbers[x] <= numbers[pivot]:
                C[i] = numbers[x]
                i+=1
            else:
                C[j] = numbers[x]
                j-=1
        C[i] = numbers[pivot]
        
        # Copy C back into numbers
        for k in range(len(numbers)):
            if C[k] is not None:
                numbers[k] = C[k]
        
        # return pivot position
        return i
    
    # Base case
    if high - low < 1:
        return
    
    # Choose pivot
    pivot = random.randint(low, high)
    numbers[high], numbers[pivot] = numbers[pivot], numbers[high]
    # Partition the array and get the current pivot position
    pivot_position = partition(numbers, low, high)
    # QuickSort left part of the array
    quickSortHelper(numbers, low, pivot_position-1)
    # Quicksort right part of the array
    quickSortHelper(numbers, pivot_position+1, high)

# Mergesort algorithm -> Worst Case Time Complexity: O(nlog(n))
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

# Heap class
# Heapsort algorithm -> Worst Case Time Complexity: O(nlog(n))
class Heap:
    def __init__(self, arr = []):
        self.initializeHeap(arr)
        
    def initializeHeap(self, arr=[]):
        self.size = 0
        self.heap = []
        self.heap.append(None)
        for x in arr:
            self.heap.append(x)
            self.size+=1
        if self.size > 1:
            self.buildMaxHeap()
            
    # returns parent position of i
    def parent(self, i):
        return int(i/2)
    
    # returns left child
    def left(self, i):
        return 2*i
    
    # returns right child
    def right(self, i):
        return 2*i + 1
    
    def buildMaxHeap(self):
        i = int(self.size/2)
        while i >= 1:
            self.sink(i)
            i-=1
    
    def heapSort(self, arr):
        if(len(arr) < 1):
            return
        self.initializeHeap(arr)
        
        for i in range(self.size, 1, -1):
            self.heap[1], self.heap[i] = self.heap[i], self.heap[1]
            self.size -= 1
            self.sink(1)
            
        # Recover lost size during heapsort
        self.size = len(self.heap)-1
        for i in range(1, self.size+1):
            arr[i-1] = self.heap[i]
    
    def add (self, val):
        self.heap.append(val)
        self.size += 1
        #print(" quiero aniadir el ", val, " en pos", self.size)
        self.swim(self.size)
        
    def swim (self, i):
        while i > 1 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
    
    def extractMax(self):
        if self.size < 1:
            return None
        min = self.heap[1]
        self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
        self.heap.pop()
        self.size -= 1
        self.sink(1)
        return min
    
    def sink(self, i):
        while self.left(i) <= self.size:
            largest = self.left(i)
            if self.right(i) <= self.size and self.heap[largest] < self.heap[self.right(i)]:
                largest = self.right(i)
            if self.heap[i] > self.heap[largest]:
                break
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            i = largest
    
    def __str__ (self):
        res = "(" 
        for x in self.heap:
            res += str(x) + ", " 
        return res + ")"

# Radix Sort, works only for integer unsigned numbers
# Radix sort algorithm -> Worst Case Time Complexity: O(kn)
def radixSort(numbers):
    counting = []
    for i in range(11):
        counting.append(Queue());
    decimals = len(str(max(numbers)))
    
    for i in range (decimals):
        for number in numbers:
            digit = (number // 10**i)
            if(digit < 0):
                digit = -1;
            else:
                digit %= 10
            counting[digit+1].put(number)
        # dequee
        index = 0
        for x in counting:
            while not x.empty():
                numbers[index] = x.get()
                index += 1
        
numbers = [45, 30, 59, 12, 66, 23 ]
selectionSort(numbers)
print(numbers)