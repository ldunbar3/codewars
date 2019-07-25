# https://www.codewars.com/kata/flatten-me/train/python

def flatten_me(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            for j in i:
                result.append(j)
        else:
            result.append(i)
    return result