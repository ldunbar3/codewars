# https://preview.codewars.com/kata/rot13-1/train/python

import string

def rot13(message):
    k = 13
    transtab = str.maketrans(
        string.ascii_letters,
        (string.ascii_lowercase * 2)[k % 26:k % 26 + 26] + (string.ascii_uppercase * 2)[k % 26:k % 26 + 26])
    return message.translate(transtab)

print(rot13('This is a test of the emergency broadcast system.'))