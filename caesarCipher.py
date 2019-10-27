# Caesar Cipher

import pyperclip

# The string/message to be encrypted/decrypted:
message = 'This is my secret message.'

# The encryption key"
key = 13

# Wheather the program encrypts or decrypts:
mode = 'encrypt' # Set to eiterh encrypt or decrypt.

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store encrypted/decrypted form.
translated = ''