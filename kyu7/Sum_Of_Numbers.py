# https://www.codewars.com/kata/beginner-series-number-3-sum-of-numbers/train/python

'''
Given two integers a and b, which can be positive or negative, find the sum of all the numbers between 
including them too and return it. If the two numbers are equal return a or b.
'''

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))