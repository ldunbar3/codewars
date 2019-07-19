# https://www.codewars.com/kata/maximum-product/train/python

def adjacent_element_product(array):
    result = []
    for i in range(0,len(array)-1):
        result.append(array[i] * array[i+1])
    return max(result)
