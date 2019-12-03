

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