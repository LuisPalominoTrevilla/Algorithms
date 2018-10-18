def prep(arrayA):
    for i in range(1, len(arrayA)):
        arrayA[i] = arrayA[i]+arrayA[i-1]
def sumRange(start, end, sums):
    return sums[end] if start == 0 else sums[end]-sums[start-1]
arrayA = [1,-2,3,10,-8,0]
prep(arrayA)
print(sumRange(1,3, arrayA))