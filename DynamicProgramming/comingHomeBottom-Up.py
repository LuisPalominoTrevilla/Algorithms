def getPossiblePaths(n, m):
    path = [[0 for j in range(m)] for i in range(n)]
    # Base case
    for i in range(n):
        path[i][0] = 1
    for j in range(m):
        path[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            path[i][j] = path[i][j-1]+path[i-1][j]
    return path[n-1][m-1]
print(getPossiblePaths(3,3))