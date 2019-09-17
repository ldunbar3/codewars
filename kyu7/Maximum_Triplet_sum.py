# https://www.codewars.com/kata/maximum-triplet-sum-array-series-number-7/train/python

'''
Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .
'''

def max_tri_sum(numbers):
    return sum(sorted(list(set(numbers)))[-3:])