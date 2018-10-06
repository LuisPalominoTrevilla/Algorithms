# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 00:43:29 2018

@author: Luis Palomino
"""

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add(self, val):
        self.size += 1
        newNode = Node(val)
        newNode.setNext(self.head)
        self.head = newNode
    
    def addAt(self, val, pos):
        if pos <= self.size:
            if pos == 0:
                self.add(val)
                return True
            newNode = Node(val)
            curr = self.head
            prev = None
            for i in range(pos):
                prev = curr
                curr = curr.getNext()
            if curr == None:
                prev.setNext(newNode)
            else:
                newNode.setNext(curr)
                prev.setNext(newNode)
            return True
        else:
            return False
    
    def pop(self):
        if self.size >= 1:
            popNode = self.head
            self.head = self.head.getNext()
            self.size -= 1
            return popNode
        else:
            return None

    def __str__(self):
        curr = self.head
        lista = ""
        while curr is not None:
            lista += str(curr.value) + "-> "
            curr = curr.getNext()
        lista += "*"
        return lista
    
class Node:
    def __init__(self,val = None):
        self.right = None
        self.value= val
    
    def getNext(self):
        return self.right
    
    def setNext(self, new):
        self.right = new

lista = LinkedList()
lista.add(4)
lista.add(5)
lista.add(7)
lista.addAt(10, 3)
print(lista)