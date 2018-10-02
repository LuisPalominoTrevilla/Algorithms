def getLargestSum(a):
    curr_sum, max_sum = 0, 0
    for num in a:
        curr_sum += num
        if curr_sum < 0:
            curr_sum = 0
        if curr_sum > max_sum:
            max_sum = curr_sum 
    return max_sum
a = [10,-2, -3, 4, -1, -8, -2, 1, 5, -3]
print(getLargestSum(a))