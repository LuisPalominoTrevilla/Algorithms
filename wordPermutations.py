# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:12:34 2018

@author: Luis Palomino
"""

def permutate(word, i = 0, permutations = list()):
    if type(word) is str:
        word = list(word)
    n = len(word)
    # base case
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
            """
                The following line would be an easier way of solving it without
                using more space and spending less time. It would produce the same results
                I decided not to use the next line so it could be easier to understand
                the process.
            """ 
            #word[i], word[char] = word[char], word[i]
    return permutations

print(permutate("xyz"))