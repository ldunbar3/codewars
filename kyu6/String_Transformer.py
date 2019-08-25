# https://www.codewars.com/kata/string-transformer/train/python

def string_transformer(s):
    s = s.split(" ")
    return ' '.join(reversed(s)).swapcase()