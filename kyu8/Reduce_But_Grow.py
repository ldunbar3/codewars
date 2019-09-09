# https://www.codewars.com/kata/beginner-reduce-but-grow/train/python

'''
Given a non-empty array of integers, return the result of multiplying the values 
together in order.
'''

def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result