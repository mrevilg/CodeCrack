# Reverse Cipher

message = 'Three can keep a secret, if tewo of them are dead.'
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i -1

print(translated)