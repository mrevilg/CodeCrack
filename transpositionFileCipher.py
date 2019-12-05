

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'frankenstein.txt'
    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt' # Set to encrypt or decrypt

    if not os.path.exists(inputFilename):
        print('This file %s does not exist, hold for processing...'
        % (inputFilename))
        sys.exit()

    if os.path.exists(outputFilename):
        print('This will overwrite this file %s. (C)ontinue or (Q)uit' %
            (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))