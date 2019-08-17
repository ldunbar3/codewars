# https://www.codewars.com/kata/sum-of-intervals/train/python

def sum_of_intervals(intervals):
    result = []
    for i in intervals:
        for j in range(i[0],i[1]):
            result.append(j)
    return len(set(result))

print(sum_of_intervals([(1, 5)]))#, 4)
print(sum_of_intervals([(1, 5), (6, 10)]))#, 8)
print(sum_of_intervals([(1, 5), (1, 5)]))#, 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))#, 7)