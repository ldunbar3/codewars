# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
from math import sqrt
from itertools import count, islice

def is_prime(num):
    if num < 2:
        return False
    for i in islice(count(2), int(sqrt(num) - 1)):
        if num % i == 0:
            return False
    return True