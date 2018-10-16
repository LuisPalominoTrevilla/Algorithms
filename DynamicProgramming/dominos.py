def dominos(n, memo=None):
    if not memo:
        memo = [None]*n
    if n == 0:
        return 1
    elif n < 0:
        return 0
    if memo[n-1] is not None:
        return memo[n-1]
    memo[n-1] = dominos(n-1, memo)+dominos(n-2, memo)
    return memo[n-1]
print(dominos(3))