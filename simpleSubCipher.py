
import pyperclip, sys, random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = """If a man is offered a fact which goes against his instincts, 
        he will scrutinize it closely, and unless the evidence is overwhelming, 
        he will refuse to believe it. If, on the other hand, he is offered something 
        which affords a reason for acting in accordance to his instincts, 
        he will accept it even on the slightest evidence. 
        The origin of myths is explained in this way. -Bertrand Russell"""
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'encrypt' # Set to encrypt or decrypt

    if keyIsValid(myKey):
        sys.exit('There is an error in the key or symbol set.')