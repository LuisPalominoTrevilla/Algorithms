import math
def sieve(primes):
    real_primes = []
    for i in range(2, x2+1):
        if primes[i]:
            real_primes.append(i)
            for j in range(i*2, x2+1, i):
                primes[j] = False
    return real_primes
def getX0(x2):
    hash_primes = [True]*(x2+1)
    primes = sieve(hash_primes)
    largest = 2
    for prime in primes:
        if prime > x2:
            break
        if not x2%prime and prime > largest:
            largest = prime
    lower_bound = x2-largest+1
    
x2 = int(input())
print(getX0(x2))