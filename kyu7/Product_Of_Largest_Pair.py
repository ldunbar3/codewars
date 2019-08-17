# https://www.codewars.com/kata/product-of-largest-pair/train/python

def max_product(a):
    y = max(a)
    a.remove(y)
    z = max(a)
    return y * z