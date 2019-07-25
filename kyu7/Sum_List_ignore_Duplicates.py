# https://www.codewars.com/kata/sum-a-list-but-ignore-any-duplicates/train/python

def sum_no_duplicates(l):
    result = []
    for i in l:
        if l.count(i) <= 1: result.append(i) 
    return sum(result)