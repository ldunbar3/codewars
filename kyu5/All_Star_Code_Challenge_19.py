# https://www.codewars.com/kata/all-star-code-challenge-number-19/train/python

from itertools import permutations

def slogan_maker(array):
    tmp = []
    result = []
    for i in array:
        if i not in tmp:
            tmp.append(i)
    tmp = list(permutations(tmp))
    for i in tmp:
        result.append(' '.join(i))
    return result