
import sys, pyperckip, cryptomath, random
SYMBOLS = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop
            qrstuvwxyz1234567890 !?."""

def main():
    myMessage = """ "A computer would deserve to be called intelligent
        if it could deceive a human into believing it was human."
        -Alan Turing"""
    myKey = 2894
    myMode = 'encrypt' # Set to either encrypt or decrypt.

    if myMode == 'encrypt':
        translated = encryptedMessage(myKey, myMessage)
    elif myMode == 'decrypt'