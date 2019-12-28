
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
    print
    print
    print
    pyperclip.copy(translated)
    print('Full %sed text to clipboard.' % (myMode))