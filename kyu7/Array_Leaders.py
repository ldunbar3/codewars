# https://www.codewars.com/kata/array-leaders-array-series-number-3/train/python

def array_leaders(numbers):
    results = []
    for k, v in enumerate(numbers):
        if v > sum(numbers[k+1:]):
            results.append(v)
    return results