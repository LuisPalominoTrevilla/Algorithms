import math
def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    m = int(math.sqrt(n))
    inc = 4
    for i in range(5, m+1, inc):
        if n % i == 0:
            return False
        inc = 6 - inc
    return True

def sieveEratosthenes(n):
    for i in range(1, n+1):
        if isPrime(i):
            print(i)

n = int(input())
sieveEratosthenes(n)