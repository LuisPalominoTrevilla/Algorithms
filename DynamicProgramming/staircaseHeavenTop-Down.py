def staircase(n, memo=None):
    if not memo:
        memo = [None]*n
    if n == 0:
        return 1
    elif n < 0:
        return 0
    if memo[n-1] is not None:
        return memo[n-1]
    print(n)
    memo[n-1] = staircase(n-1, memo)+staircase(n-2, memo)
    return memo[n-1]
print(staircase(50))