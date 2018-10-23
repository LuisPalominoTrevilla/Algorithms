import math
def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n==1 or n % 2 == 0 or n % 3 == 0:
        return False
    m = int(math.sqrt(n))
    inc = 4
    for i in range(5, m+1, inc):
        if n % i == 0:
            return False
        inc = 6 - inc
    return True

def primeNumbers(num):
    assert len(num) >= 3
    dp = [0]*(len(num)+1)
    i = 1
    for digit in num:
        dp[i] = int(digit) + dp[i-1]
        if i - 3 >= 0:
            number = dp[i] - dp[i-3]
            if not isPrime(number):
                return False
        if i - 4 >= 0:
            number = dp[i] - dp[i-4]
            if not isPrime(number):
                return False
        if i - 5 >= 0:
            number = dp[i] - dp[i-5]
            if not isPrime(number):
                return False
        i+=1
    return True

num = input()
print(primeNumbers(num))