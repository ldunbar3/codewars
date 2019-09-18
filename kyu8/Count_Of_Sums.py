# https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives/train/python

'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second 
element is sum of negative numbers.

If the input array is empty or null, return an empty array.
'''

def count_positives_sum_negatives(arr):
    pos_count = 0
    neg_sum = 0

    if not arr:
        return []

    for i in arr:
        if i > 0:
            pos_count += 1
        else:
            neg_sum += i
    return [pos_count, neg_sum]