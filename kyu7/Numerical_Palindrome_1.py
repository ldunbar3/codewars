# https://www.codewars.com/kata/numerical-palindrome-number-1/train/python

def palindrome(num):

    if type(num) == int:
        if num > 0:
            return num == int(str(num)[::-1])
    return "Not valid"