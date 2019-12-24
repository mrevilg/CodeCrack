

def gcd(a, b):
    # Return the GCD of a and b using Euclids algorithm:
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    # Return the modular inverse of a % m, which is
    # the number x such that a*x % m =1.

    if gcd(a, m) != 1:
        return None