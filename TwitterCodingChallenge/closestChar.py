import math
def closest(s, queries):
    positions = {}
    result = []
    for i in range(len(s)):
        if positions.get(s[i]):
            positions[s[i]].append(i)
        else:
            positions[s[i]] = [i]
    for index in queries:
        letter = s[index]
        pos = positions[letter]
        if (len(pos) == 1):
            result.append(-1)
        else:
            tmp = bs(pos, index)
            closest = None
            if tmp == 0:
                closest = pos[1]
            elif tmp == len(pos)-1:
                closest = pos[tmp-1]
            else:
                closest = pos[tmp-1] if abs(pos[tmp-1]-index) <= abs(pos[tmp+1]-index) else pos[tmp+1]
            result.append(closest)
    return result
def bs(array, element):
    low = 0
    high = len(array)-1
    while(high >= low):
        mid = (low+high)//2
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            high = mid
        elif array[mid] < element:
            low = mid+1
print(closest('sam', [1]))