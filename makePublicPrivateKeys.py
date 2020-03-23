

import random, sys, os, primeNum, cryptomath

def main():
    print('Making key files...')
    makeKeyFiles('al_sweigart', 1024)
    print('Key files made.')

def generateKey(keysize):
    p = 0
    q = 0

    print('Generating p prime...')
    while p == q:
        p = primeNum.generateLargePrime(keysize)
        q = primeNum.generateLargePrime(keysize)
    n = p * q

    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    print('Calculating d that is mod inverse of e...')
    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))    

    publicKey = (n,e)
    privateKey = (n,d)

    print('Public key:', publicKey)
    print('Private key:', privateKey)

    return (publicKey, privateKey)

def makeKeyFiles(name, keySize):
    if os.path.exists('%s_pubkey.txt' % (name)) or
    os.path.exists('%s_privkey.txt' % (name)):
    sys.exit()

        
