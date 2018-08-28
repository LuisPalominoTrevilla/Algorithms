# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:12:34 2018

@author: Luis Palomino
"""

def permutate(word, i = 0, permutations = list()):
    if type(word) is str:
        word = list(word)
    # base case
    n = len(word)
    if i == n-1:
        permutations.append(''.join(word))
        return
    else:
        for char in range (i, n):
            # Remember the current state of the word
            tmp = word[:]
            # Swap every character with the ith one
            word[i], word[char] = word[char], word[i]
            # permutate rest of characters recursively
            permutate(word, i+1, permutations)
            # Change the word to its state before the recursive permutations
            word = tmp[:]
    return permutations

print(permutate("abc"))