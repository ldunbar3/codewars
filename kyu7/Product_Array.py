# https://preview.codewars.com/kata/product-array-array-series-number-5/train/python

def product_array(numbers):
    product_arr = []
    for i in range(len(numbers)):
        p = 1
        result = (numbers[:i] + numbers[i+1:])
        for i in result:
            p *= i
        product_arr.append(p)
    return product_arr
