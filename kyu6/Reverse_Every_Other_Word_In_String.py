# https://www.codewars.com/kata/reverse-every-other-word-in-the-string/train/python

def reverse_alternate(string):
    s = string.split()
    for i in range(0,len(s)):
        if i % 2 != 0:
            s[i] = s[i][::-1]
    return ' '.join(s)