# https://www.codewars.com/kata/tidy-number-special-numbers-series-number-9/train/python

def tidyNumber(n):
    return sorted([int(x) for x in str(n)]) == [int(x) for x in str(n)]