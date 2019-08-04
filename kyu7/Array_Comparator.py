# https://www.codewars.com/kata/array-comparator/train/python

def match_arrays(v, r):
    result = 0
    for item in v:
        if r.count(item) > 0:
            result += 1
    return result

# DON'T remove
verbose = True # set to True to diplay arrays being tested in the random tests