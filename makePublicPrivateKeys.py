

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
        
        
