def getPossibleSuffixes(s):
    if len(s) == 5:
        print(0)
        return
    possible_suffixes = s[5:len(s)]
    suffixes = []
    visited = {}
    helper(possible_suffixes, len(possible_suffixes)-1, suffixes, 1, "", visited)
    helper(possible_suffixes, len(possible_suffixes)-1, suffixes, 2, "", visited)
    print(len(suffixes))
    suffixes.sort()
    for s in suffixes:
        print(s)
def helper(s,i, suffixes, quantity, prev, visited):
    if i - quantity >= 0 and s[i-quantity:i+1] != prev and not visited.get(str(i)+str(quantity)):
        visited[str(i)+str(quantity)] = True
        if s[i-quantity:i+1] not in suffixes: suffixes.append(s[i-quantity:i+1])
        helper(s, i-quantity-1, suffixes, 1, s[i-quantity:i+1], visited)
        helper(s, i-quantity-1, suffixes, 2, s[i-quantity:i+1], visited)
    else:
        return
s = input()
getPossibleSuffixes(s)