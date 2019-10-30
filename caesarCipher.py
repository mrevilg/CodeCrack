# Caesar Cipher

import pyperclip

# Select the string/message to be encrypted/decrypted:
message = 'This is my secret message.'
message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

# The encryption key"
key = 13

# Wheather the program encrypts or decrypts:
mode = 'decrypt' # Set to either encrypt or decrypt.

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store encrypted/decrypted form.
translated = ''

for symbol in message:
    # Note: Only symbols in SYMBOLS can be recognized
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption:
        if mode =='encrypt':
            translateIndex = symbolIndex + key
        elif mode == 'decrypt':
            translateIndex = symbolIndex - key

        # Handle wraparound, if needed:
        if translateIndex >= len(SYMBOLS):
            translateIndex = translateIndex - len(SYMBOLS)
        elif translateIndex < 0:
            translateIndex = translateIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translateIndex]
    else:
        # Append the symbol without encryption/decryption:
        translated = translated + symbol

# Output the translated string:
print(translated)
pyperclip.copy(translated)
