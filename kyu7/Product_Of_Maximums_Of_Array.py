# https://www.codewars.com/kata/product-of-maximums-of-array-array-series-number-2/train/python

def max_product(lst, n_largest_elements):
    largest_items = sorted(lst)[-n_largest_elements:]
    product = 1
    for number in largest_items:
        product *= number
    return product