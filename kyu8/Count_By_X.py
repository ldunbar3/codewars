# https://www.codewars.com/kata/count-by-x/train/python

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """

    return list(range(x, x * n + 1, x))