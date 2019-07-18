# https://preview.codewars.com/kata/alphabetized/train/python

def alphabetized(s):
    result = ""
    for c in s:
        if c.isalpha() == True:
            result += c
    return ''.join(sorted(result, key=lambda s: s.lower()))




print(alphabetized("CodeWars can't Load Today"))