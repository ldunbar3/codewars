# https://www.codewars.com/kata/minimum-steps-array-series-number-6/train/python

def minimum_steps(numbers, value):
    numbers = sorted(numbers)
    s = 0
    for k, v in enumerate(numbers):
        s += v
        if s >= value: return k