# https://www.codewars.com/kata/5566b0dd450172dfc4000005

'''
As part of this Kata, you need to find the length of the sequence in an array, between 
the first and the second occurrence of a specified number.
'''

def length_of_sequence(arr,n):
    if n in arr and len(arr) > 1 and arr.count(n) == 2:
        start = arr.index(n)
        end = len(arr) - 1 - arr[::-1].index(n)
        return (end - start) + 1
    else:
        return 0