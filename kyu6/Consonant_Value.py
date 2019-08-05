# https://www.codewars.com/kata/consonant-value/train/python

'''
Given a lowercase string that has alphabetic characters only and no spaces, return the highest
value of consonant substrings. Consonants are any letters of the alpahabet except "aeiou".
'''
import re
def solve(s):
    return max(sum(ord(char) for char in word) - (len(word) * 96) for word in re.findall('[^aeiou]+', s))