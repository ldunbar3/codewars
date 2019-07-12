# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

import string

def is_pangram(s):
    s = s.upper().replace(" ", "")
    string = ""
    for c in s:
        if c.isalpha():
            string = string + c
    print(string, " ", len(sorted(set(string))))
    print(s)
    return True if len(sorted(set((string)))) == 26 else False

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("A gopro"))
