

def gcd(a, b):
    # Return the GCD of a and b using Euclids algorithm:
    while a != 0:
        a, b = b % a, a
    return b