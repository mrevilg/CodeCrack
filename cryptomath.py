

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
    
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # Note: // is the int division operator.
        v1, v2, v3, u1, u2, u3, = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
