

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