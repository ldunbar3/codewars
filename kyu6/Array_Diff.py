# https://www.codewars.com/kata/array-dot-diff/train/python

'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b.
'''

def array_diff(a, b):
    result = []
    for i in a:
        if b.count(i) == 0:
            result.append(i)
    return result