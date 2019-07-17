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


print(product_array([12,20]))#, [20,12])
print(product_array([12,20]))#, [20,12])
print(product_array([3,27,4,2]))#, [216,24,162,324])
print(product_array([13,10,5,2,9]))#, [900,1170,2340,5850,1300])
print(product_array([16,17,4,3,5,2]))#, [2040,1920,8160,10880,6528,16320])