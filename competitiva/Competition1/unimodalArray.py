def isUnimodal(n, a):
    state = 0
    for i in range(1, n):
        if state == 0:
            if a[i-1] > a[i]:
                state = 2
            if a[i-1] == a[i]:
                state = 1
        elif state == 1:
            if a[i-1] < a[i]:
                return 'NO'
            if a[i-1] > a[i]:
                state = 2
        elif state == 2:
            if a[i-1] <= a[i]:
                return 'NO'
    return 'YES'
n = int(input())
a = [int(x) for x in input().split()]
print(isUnimodal(n, a))