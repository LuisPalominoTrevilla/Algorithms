class MinHeap:
    def __init__(self, arr = []):
        self.initializeHeap(arr)
        
    def initializeHeap(self, arr=[]):
        self.size = 0
        self.heap = []
        self.heap.append(None)

    # returns parent position of i
    def parent(self, i):
        return int(i/2)
    
    # returns left child
    def left(self, i):
        return 2*i
    
    # returns right child
    def right(self, i):
        return 2*i + 1
    
    def insert (self, val):
        self.heap.append(val)
        self.size += 1
        self.swim(self.size)
    
    def extractMin(self):
        if self.size < 1:
            return None
        min = self.heap[1]
        self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
        self.heap.pop()
        self.size -= 1
        self.sink(1)
        return min
    
    def peekMin(self):
        return self.heap[1] if self.size >= 1 else None
    
    def extractElement(self, value):
        if self.size < 1:
            return None
        for i in range(1, self.size+1):
            if self.heap[i] == value:
                self.heap[i], self.heap[self.size] = self.heap[self.size], self.heap[i]
                self.heap.pop()
                self.size-=1
                self.sink(i)
                return value
        # No element was found
        return None
    
    def swim (self, i):
        while i > 1 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
    
    def sink(self, i):
        while self.left(i) <= self.size:
            smallest = self.left(i)
            if self.right(i) <= self.size and self.heap[smallest] > self.heap[self.right(i)]:
                smallest = self.right(i)
            if self.heap[i] < self.heap[smallest]:
                break
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            i = smallest
    
    def isEmpty(self):
        return self.size == 0

    def __str__ (self):
        res = "(" 
        for x in self.heap:
            if x is not None:
                res += str(x) + ", " 
        return res + ")"