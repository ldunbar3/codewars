# https://www.codewars.com/kata/beginner-lost-without-a-map/train/python

'''
There are more concise ways of doing this. But, the kata specifically wants you
to understand the map() function
'''


def double(n):
    return n * 2

def maps(a):
    return list(map(double, a))