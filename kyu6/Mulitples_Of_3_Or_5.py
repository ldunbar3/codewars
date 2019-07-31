# https://www.codewars.com/kata/multiples-of-3-or-5/train/python

def solution(number):
    multiple_sum = 0
    for n in range(3,number):
        if n % 3 == 0 or n % 5 == 0:
            multiple_sum += n
    return multiple_sum
