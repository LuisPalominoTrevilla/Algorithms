def getSmallestDifferNum(n, k):
    res = 0
    visited = {}
    for i in range(len(n)):
        num = int(n[i])
        if visited.get(num):
            visited[num] += 1
        else:
            visited[num] = 1
        res += num
        if res >= k:
            return 0
    acum = 0
    num_digit = 0
    for i in range(10):
        if visited.get(i):
            j = 0
            while(j < visited.get(i)):
                acum += 9-i
                num_digit += 1
                if acum + res >= k:
                    return num_digit
                j+=1
    return num_digit
k = int(input())
n = input()
print(getSmallestDifferNum(n, k))