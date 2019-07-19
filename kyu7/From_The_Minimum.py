# https://www.codewars.com/kata/form-the-minimum/train/python

def min_value(digits):
    return int(''.join(map(str,sorted(set(digits)))))
