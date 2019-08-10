# https://www.codewars.com/kata/find-the-odd-int/train/python

'''
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''

def find_it(seq):
    for i in list(set(seq)):
        if seq.count(i) % 2 != 0:
            return i