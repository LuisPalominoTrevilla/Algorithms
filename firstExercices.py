import matplotlib.pyplot as plt
import time
from random import randint

#Complejidad O(1)
def returnfirst(lista):
    return lista[0];

#Complejidad O(n)
def printList(lista):
    for x in lista:
        print(x)

#Complejidad O(n^2)    
def productoCartesiano(lista):
    for x in lista:
        print("PRSRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR");
        for y in lista:
            print (str(x) + ", " + str(y) + "\n");

#complejidad O(n)
def completeness(text):

    if text[0] == '}' or text[0] == ']' or text[0] == ')':
        return False

    if text[len(text)-1] == '{' or text[len(text)-1] == '[' or text[len(text)-1] == '(':
        return False

    stack = []
    
    for character in text:
        if character == '{' or character == '[' or character == '(':
            if character == '{':
                stack.append('}')
            if character == '[':
                stack.append(']')
            if character == '(':
                stack.append(')')
        elif character == '}' or character == ']' or character == ')':
            if not stack:
                return False

            if stack[len(stack)-1] == character:
                stack.pop()
            else:
                return False

    return True

#Dados dos strings, checar si son anagramas; "Clint Eastwood" "Old west action"
# Complejidad O(n)
def checkAnagram(sen1, sen2):

    sen1 = sen1.lower()
    sen2 = sen2.lower()

    sen1 = sen1.replace(' ', '')
    sen2 = sen2.replace(' ', '')
    list1 = list(sen1)
    list2 = list(sen2)
    
    if len(list1) != len(list2):
        return False
    
    list1.sort()
    list2.sort()
    
    pos = 0
    igual = True
    while (pos<len(list1) and igual):
        if list1[pos] == list2[pos]:
            pos+=1
        else:
            igual = False
    return igual

def graphFirst():
    lista = []
    for i in range(1,31):
        for x in range(0, i):
            lista.append(x)
        # lista esta llena
        start_time = time.time()
        returnfirst(lista)
        elapsed_time = time.time() - start_time
        plt.scatter(i, elapsed_time)
    
    plt.show()

def graphSecond():
    lista = []
    for i in range(1,50):
        for x in range(0, i):
            lista.append(x)
        # lista esta llena
        start_time = time.time()
        printList(lista)
        elapsed_time = time.time() - start_time
        plt.scatter(i, elapsed_time)
    
    plt.show()

def graphThird():
    lista = []
    for i in range(1,31):
        for x in range(0, i):
            lista.append(x)
        # lista esta llena
        start_time = time.time()
        productoCartesiano(lista)
        elapsed_time = time.time() - start_time
        plt.scatter(i, elapsed_time)
    
    plt.show()

def graphFourth():
    parenthesis = {1:")",2:"(",3:"[",4:"]",5:"{",6:"}"}
    text=""
    for i in range(1,31):
        for x in range(0, i):
            text += parenthesis[randint(1, 6)]
        # lista esta llena
        start_time = time.time()
        completeness(text)
        elapsed_time = time.time() - start_time
        plt.scatter(i, elapsed_time)

def graphFifth():
    letters = "abcdefghijklmnopqrstuvwxyz"
    string1 = ""
    string2 = ""
    for i in range(1,31):
        for x in range(0, i):
            string1 += letters[randint(0, 25)]
            string2 += letters[randint(0, 25)]
        # lista esta llena
        print(string1)
        print("\n")
        print(string2)
        print("\n\n")
        start_time = time.time()
        checkAnagram(string1, string2)
        elapsed_time = time.time() - start_time
        plt.scatter(i, elapsed_time)
        
graphThird()