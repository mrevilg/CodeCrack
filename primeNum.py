

import math, random

def isPrimeTrialDiv(num):
    if num < 2:
        return False

    for i in range (2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primeSieve(sieveSize):
    
    sieve = [True] * sieveSize
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i
        
        primes = []
        for i in range(sieveSize):
            if sieve[i] == True:
                primes.append(i)

        return primes

def rabinMiller(num):
    if num % 2 == 0 or num <2:
        return False
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)