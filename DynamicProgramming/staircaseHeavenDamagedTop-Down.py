def staircase(n, k, memo=None):
    if not memo:
        memo = [None]*n
    if n == 0:
        return 1
    elif n < 0 or n == k:
        return 0
    if memo[n-1] is not None:
        return memo[n-1]
    memo[n-1] = staircase(n-1, k,memo)+staircase(n-2, k, memo)
    return memo[n-1]
print(staircase(5, 3))