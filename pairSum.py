def getPairSum(x, k):
    complements = set()
    for num in x:
        complement = abs(num-k)
        if complement in complements:
            return (num, complement)
        complements.add(num)
    return -1
nums = [3,4,1,2,3,8,9,7,3]
print(getPairSum(nums, 10))