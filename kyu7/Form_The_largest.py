# https://www.codewars.com/kata/form-the-largest/train/python

def max_number(n):
    return int(''.join(sorted(str(n), reverse=True)))
