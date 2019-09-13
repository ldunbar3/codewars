# https://www.codewars.com/kata/56a5d994ac971f1ac500003e

'''
You are given an array strarr of strings and an integer k. Your task is
to return the first longest string consisting of k consecutive strings taken in the array.
'''

def longest_consec(strarr, k):
    n = len(strarr)
    if k <= 0 or k > n or n == 0:
        return ""

    last_start_idx = n - k

    longest_comp = ""
    longest_comp_length = 0

    for idx, substring in enumerate(strarr[:last_start_idx + 1]):
        composite = "".join(strarr[idx:idx + k])
        composite_length = len(composite)
        if composite_length > longest_comp_length:
            longest_comp, longest_comp_length = composite, composite_length

    return longest_comp