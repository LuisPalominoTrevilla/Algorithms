def findDistinctNumbers(n, m, a, l):
    dif_numbers = [0]*n
    mapCount = {}
    for i in range(n-1, -1, -1):
        if not mapCount.get(a[i]):
            mapCount[a[i]] = 1
        else:
            mapCount[a[i]] += 1
        if i == n-1:
            dif_numbers[i] = 1
        else:
            dif_numbers[i] = dif_numbers[i+1] + (1 if mapCount[a[i]] == 1 else 0)
    for query in l:
        print(dif_numbers[query-1])
n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
l = []
for i in range(m):
    l.append(int(input()))
findDistinctNumbers(n, m, a, l)