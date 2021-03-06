# Each character on a computer is assigned a unique code and the preferred 
# standard is ASCII (American Standard Code for Information Interchange). For 
# example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
# 
# A modern encryption method is to take a text file, convert the bytes to 
# ASCII, then XOR each byte with a given value, taken from a secret key. The 
# advantage with the XOR function is that using the same encryption key on 
# the cipher text, restores the plain text; for example, 65 XOR 42 = 107, 
# then 107 XOR 42 = 65.
# 
# For unbreakable encryption, the key is the same length as the plain text 
# message, and the key is made up of random bytes. The user would keep the 
# encrypted message and the encryption key in different locations, and 
# without both "halves", it is impossible to decrypt the message.
# 
# Unfortunately, this method is impractical for most users, so the modified 
# method is to use a password as a key. If the password is shorter than the 
# message, which is likely, the key is repeated cyclically throughout the 
# message. The balance for this method is using a sufficiently long password 
# key for security, but short enough to be memorable.
# 
# Your task has been made easy, as the encryption key consists of three lower 
# case characters. Using cipher1.txt (right click and 'Save Link/Target 
# As...'), a file containing the encrypted ASCII codes, and the knowledge 
# that the plain text must contain common English words, decrypt the message 
# and find the sum of the ASCII values in the original text.

import string
from itertools import product, cycle, izip, islice

def decode(text, decoder):
    for char, cipher in izip(text, decoder):
        yield chr(char ^ cipher)

def decrypt(key_len, key_seq, text):
    possible_keys = product(key_seq, repeat=key_len)

    printable_chars = set(string.printable)
    letters = set(string.ascii_letters)

    for key in possible_keys:
        decoder = cycle( ord(letter) for letter in key )

        decoded = ''.join(decode(text,decoder))

        if not set(decoded).issubset(printable_chars):
            continue

        if decoded.count(' the ') > 3:
            return (''.join(key), decoded)

if __name__ == "__main__":
    f = open('cipher1.txt','r')
    text = [ int(n) for n in f.read().split(',') ]
    key_seq = string.ascii_lowercase
    key, decoded_text = decrypt(3, key_seq, text)
    print decoded_text
    print 'Key:', key
    print 'Sum:', sum( ord(letter) for letter in decoded_text )
