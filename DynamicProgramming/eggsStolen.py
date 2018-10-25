def findMaxEggs(x):
    dp = [[0 for i in range(len(x))] for j in range(2)]
    dp[0][0] = 0
    dp[1][0] = x[0]
    for i in range(1, len(x)):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1])
        dp[1][i] = x[i]+dp[0][i-1]
    return max(dp[0][-1], dp[1][-1])
x = [10,10,9,100,3]
print(findMaxEggs(x))