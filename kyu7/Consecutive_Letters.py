# https://www.codewars.com/kata/consecutive-letters/train/python

'''
n this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet
and if each letter occurs only once.
'''

def solve(string):
    string = sorted([ord(char) for char in string])
    return True if string[-1] - string[0] == len(string)-1 else False