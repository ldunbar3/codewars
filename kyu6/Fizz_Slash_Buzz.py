# https://www.codewars.com/kata/fizz-slash-buzz/train/python

'''
Write a function that takes an integer and returns an array [A, B, C], where A is the
number of multiples of 3 (but not 5) below the given integer, B is the number of multiples
of 5 (but not 3) below the given integer and C is the number of multiples of 3 and 5 below
the given integer.
'''

def solution(number):
    a, b, c = 0, 0, 0
    for i in range(1, number):
        if i % 15 == 0:
            c += 1
        elif i % 5 == 0:
            b += 1
        elif i % 3 == 0:
            a += 1
    return [a,b,c]