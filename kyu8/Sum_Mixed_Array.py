# https://www.codewars.com/kata/sum-mixed-array/train/python

'''
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
'''

def sum_mix(arr):
    return sum(map(int, arr))