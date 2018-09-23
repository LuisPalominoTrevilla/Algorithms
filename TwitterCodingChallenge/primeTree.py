# Complete the primeQuery function below.
import math
remember_primes = {}
class Node:
    def __init__(self, node, value):
        self.node = node
        self.value = value
        self.prime = self.isPrime(value)
        remember_primes[value] = self.prime
        self.parent = None
        self.neighbors = []
    
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)
        
    def setParent(self, parent):
        self.parent = parent
    
    # Used to see if a number is prime using the Sieve of Eratosthenes
    def isPrime(self, n):
        if remember_primes.get(n):
            return remember_primes[n]
        if n == 2 or n == 3:
            return True
        if n==1 or n % 2 == 0 or n % 3 == 0:
            return False
        m = int(math.sqrt(n))
        inc = 4
        for i in range(5, m+1, inc):
            if n % i == 0:
                return False
            inc = 6 - inc
        return True
    
def primeQuery(n, first, second, values, queries):
    vertices = [None]*(n+1)
    output = []
    for i in range(len(first)):
        if not vertices[first[i]]:
            vertices[first[i]] = Node(first[i], values[first[i]-1])
        if not vertices[second[i]]:
            vertices[second[i]] = Node(second[i], values[second[i]-1])
        vertices[first[i]].addNeighbor(vertices[second[i]])
        vertices[second[i]].addNeighbor(vertices[first[i]])
    # Assign parent to each node except node 1
    visit = []
    visit.append(vertices[1])
    while(len(visit) > 0):
        curr_node = visit.pop()
        for neighbor in curr_node.neighbors:
            if curr_node.parent is not neighbor:
                neighbor.setParent(curr_node)
                visit.append(neighbor)
    # Search number of prime children
    for index_node in queries:
        num_primes = 0
        visit = []
        visit.append(vertices[index_node])
        while(len(visit) > 0):
            curr_node = visit.pop()
            # If value of current node is prime sum it
            num_primes += 1 if curr_node.prime else 0
            for neighbor in curr_node.neighbors:
                if curr_node.parent is not neighbor:
                    visit.append(neighbor)
        output.append(num_primes)
    return output
    