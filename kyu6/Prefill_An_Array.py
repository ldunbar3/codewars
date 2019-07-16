# https://www.codewars.com/kata/prefill-an-array/train/python

def prefill(n, v='undefined'):
    if n is None:
        raise TypeError("None is invalid")
    try:
        n = int(n)
    except ValueError:
        raise TypeError(n + " is invalid")
    return [v] * n