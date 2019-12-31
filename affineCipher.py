
import sys, pyperclip, cryptomath, random
SYMBOLS = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop
            qrstuvwxyz1234567890 !?."""

def main():
    myMessage = """ "A computer would deserve to be called intelligent
        if it could deceive a human into believing it was human."
        -Alan Turing"""
    myKey = 2894
    myMode = 'encrypt' # Set to either encrypt or decrypt.

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Key: %s' % (myKey))
    print('%sed text:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text to clipboard.' % (myMode))

def getKeyParts(key):
    keyA = key // len (SYMBOLS)
    keyB = key % len(SYMBOLS)
    return(keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if A is 1. Choose another key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if B is 0. Choose another key.')
            