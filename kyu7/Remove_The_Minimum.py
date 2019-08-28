# https://www.codewars.com/kata/remove-the-minimum/train/python

'''
Given an array of integers, remove the smallest value. Do not mutate the original array/list.
If there are multiple elements with the same value, remove the one with a lower index. If you get
an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.
'''

def remove_smallest(numbers):
    result = numbers.copy()
    if numbers:
        result.pop(result.index(min(result)))
    return result

print(remove_smallest([1, 2, 3, 4, 5]))#, [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
print(remove_smallest([5, 3, 2, 1, 4]))#, [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
print(remove_smallest([1, 2, 3, 1, 1]))#, [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
print(remove_smallest([]))#, [], "Wrong result for []")