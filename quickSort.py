import statistics
def quickSort(x, l, h):
    comparisons = 0
    # Choose pivot
    if h-l <= 1:
        return 0
    comparisons = (h-l)-1
    mid = (l + h-1)//2
    tmp = [x[l], x[mid], x[h-1]]
    pivot = x.index(statistics.median(tmp))
    #pivot = l
    x[l], x[pivot] = x[pivot], x[l]
    pivot_position = partition(x, l, h)
    comparisons += quickSort(x, l, pivot_position)
    comparisons += quickSort(x, pivot_position+1, h)
    return comparisons
def partition(x, l, h):
    p = x[l]
    i = l+1
    for j in range(l+1,h):
        if x[j] < p:
            x[i], x[j] = x[j], x[i]
            i+=1
    x[l], x[i-1] = x[i-1], x[l]
    return i-1

integers = open("./quicksort.txt", "r")
x = []
for integer in integers:
    x.append(int(integer.rstrip()))
print(quickSort(x, 0, len(x)))