# https://www.codewars.com/kata/sum-of-odd-numbers/train/python

def row_sum_odd_numbers(n):
    result = 0
    step = n * (n-1) + 1
    for i in range(n):
        result += step
        step += 2
    return result