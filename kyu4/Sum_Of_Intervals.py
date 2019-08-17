# https://www.codewars.com/kata/sum-of-intervals/train/python

def sum_of_intervals(intervals):
    result = []
    for i in intervals:
        for j in range(i[0],i[1]):
            result.append(j)
    return len(set(result))