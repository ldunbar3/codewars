# https://www.codewars.com/kata/minimize-sum-of-array-array-series-number-1/train/python

'''
Given an array of intgers , Find the minimum sum which is obtained from summing each Two integers product .
Minimum Product of a list = largest integer * smallest integer
'''

def min_sum(arr):
    product_array = []
    while len(arr) != 0:
        product_array.append(max(arr) * min(arr))
        arr.remove(max(arr))
        arr.remove(min(arr))
    return sum(product_array)