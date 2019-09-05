# https://www.codewars.com/kata/opposite-array/train/python

'''
Given an array of numbers, create a function called oppositeArray that returns an array
of numbers that are the additive inverse (opposite or negative) of the original. If the
original array is empty, return it.
'''

def opposite_list(numbers):
    return [-i for i in numbers]