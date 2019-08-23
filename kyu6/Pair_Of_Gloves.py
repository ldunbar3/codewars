# https://www.codewars.com/kata/58235a167a8cb37e1a0000db

'''
You are given an array containing the color of each glove.
You must return the number of pair you can constitute.
You must not change the input array.
'''

def number_of_pairs(gloves):
    pair_result = {}
    for glove in list(set(gloves)):
        pair_result[glove] = gloves.count(glove) // 2
    return sum(pair_result.values())