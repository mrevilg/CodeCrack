import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = dectyptMessage(myKey, myMessage)

    print(plaintext + '|')

    pyperclip.copy(plaintext)