import math
def staircase(n, costs):
    cost.append(0)
    memo = [None for i in range(n+1)]
    return helper(n, costs, memo)
def helper(level, costs, memo):
    if level == 0:
        memo[level] = costs[level]
        return memo[level]
    if level < 0:
        return math.inf
    if memo[level] is None:
        memo[level] = costs[level] + min(helper(level-1, costs, memo), helper(level-2, costs, memo), helper(level-3, costs, memo))
    return memo[level]
cost = [1,1,1,3]
print(staircase(4, cost))