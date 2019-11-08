import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')

    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex excceds message length:
        while currentIndex < len(message):
            # Append column end to list:
            ciphertext[column] += message[currentIndex]

            # Move currentIndex over:
            currentIndex += key