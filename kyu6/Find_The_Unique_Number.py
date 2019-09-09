# https://www.codewars.com/kata/find-the-unique-number-1/train/python

def find_uniq(arr):
    uniques = list(set(arr))

    for i in uniques:
        if arr.count(i) == 1:
            return i