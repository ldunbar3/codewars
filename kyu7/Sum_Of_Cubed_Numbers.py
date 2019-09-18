# https://www.codewars.com/kata/sum-of-odd-cubed-numbers/train/python

'''
Find the sum of the odd numbers within an array, after cubing the initial integers. The function 
should return undefined/None/nil/NULL if any of the values aren't numbers. 
'''

def cube_odd(arr):
    result = 0
    for i in arr:
        if type(i) == int:
            if i % 2 != 0:
                result += i ** 3
        else:
            return None
    return result