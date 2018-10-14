def prep(arrayA):
    sums = [[arrayA[j] if j == i else 0 for j in range(len(arrayA))] for i in range(len(arrayA))]
    for j in range(len(arrayA)):
        for i in range(len(arrayA)-1,-1,-1):
            if i < j:
                sums[i][j] = sums[i][i]+sums[i+1][j]
    return sums
def sumRange(start, end, sums):
    return sums[start][end]
arrayA = [1,-2,3,10,-8,0]
sums = prep(arrayA)
print(sumRange(3,3, sums))