# https://www.codewars.com/kata/longest-vowel-chain/train/python

'''
Given a lowercase string that has alphabetic characters only and no spaces, return the length of the 
longest vowel substring.
'''

def solve(s):
    max_len = 0
    temp_len = 0
    for character in s:
        if character in "AEIOUaeiou":
            temp_len += 1
        else:
            max_len = max(max_len, temp_len)
            temp_len = 0
    return max_len
