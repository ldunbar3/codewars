# https://www.codewars.com/kata/grasshopper-summation/train/python
'''
Write a program that finds the summation of every number from 1 to num. The number will 
always be a positive integer greater than 0.
'''

def summation(n):
    result = 0
    for i in range(n+1):
        result += i
    return result
