def getPairSum(x, k):
    complements = set()
    for num in x:
        complement = k-num
        if complement != num and complement in complements:
            #print(num, ", ", complement)
            return 1
        complements.add(num)
    return 0
numbers = open("./2sum.txt", "r")
x = []
for num in numbers:
    x.append(int(num))
num = 0
for t in range(-10000,10001):
    print(t)
    num += getPairSum(x, t)
print("result is ",num)