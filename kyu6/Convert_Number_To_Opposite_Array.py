# https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/python

def digitize(n):
    return [int(i) for i in str(n)][::-1]%