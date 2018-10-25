def getMinExchanges(x):
    count = 0
    for i in range(len(x)-2, -1, -1):
        if x[i] >= x[i+1]:
            count = 0
            for j in range(i+1, len(x)):
                if x[j] > x[j-1]:
                    break
                x[j]  = x[j-1]+1
                count+=1
    return count

x = [1,0,0,2,0,0,3]
print(getMinExchanges(x))