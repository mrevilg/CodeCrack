

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'frankenstein.encrypted.txt'
    outputFilename = 'frankenstein.decrypted.txt'
    myKey = 10
    myMode = 'decrypt' # Set to encrypt or decrypt

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

    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypted':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename,
        len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))
    
if __name__ == '__main__':
    main()