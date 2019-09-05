# https://www.codewars.com/kata/pre-fizzbuzz-workout-number-1/train/python

'''
Your inputs: a positive integer, n, greater than or equal to one. n is provided, you have NO CONTROL over its value.
Your expected outputs: an array of positive integers from 1 to n
Your job is to write an algorithm that gets you from the input to the output.
'''
def pre_fizz(n):
    return [x for x in range(1, n+1)]%