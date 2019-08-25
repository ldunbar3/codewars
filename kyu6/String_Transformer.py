# https://www.codewars.com/kata/string-transformer/train/python

'''
Given a string, return a new string that has transformed based on the input:

1. Change case of every character, ie. lower case to upper case, upper case to lower case.
2. Reverse the order of words from the input.

Note: You will have to handle multiple spaces, and leading/trailing spaces.
'''

def string_transformer(s):
    return ' '.join(reversed(s.split(" "))).swapcase()