
import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    random.seed(42)

    for i in range(20): 
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,40)

        message = list(message)
        random.shuffle(message)
        message = ''.join(message)