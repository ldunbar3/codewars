# https://www.codewars.com/kata/sum-of-minimums/train/python

'''
Given an 2D array of size m * n. Your task is to find the sum of minimum value in each row.
'''

def sum_of_minimums(numbers):
    result = 0
    for i in numbers:
        result += min(i)
    return result