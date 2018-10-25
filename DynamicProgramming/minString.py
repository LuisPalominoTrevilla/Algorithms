import math
def minString(w):
    changes = {'ab': 'c', 'ac': 'b', 'ba': 'c', 'bc': 'a', 'ca': 'b', 'cb': 'a'}
    memo = {}
    return helper(w, changes, memo)
def helper(w, changes, memo):
    minimum = math.inf
    if w.count('a') == len(w) or w.count('b') == len(w) or w.count('c') == len(w):
        memo[w] = len(w)
        return memo[w]
    for i in range(len(w)-1):
        suffix = w[i]+w[i+1]
        if suffix == 'aa' or suffix == 'bb' or suffix == 'cc':
            continue
        word = w[:i]+changes[suffix]+w[i+2:len(w)]
        if word not in memo:
            memo[word] = helper(word, changes, memo)
        if memo[word] < minimum:
            minimum = memo[word]
    return minimum
print(minString('aba'))
print(minString('bcab'))
print(minString('cab'))