# https://www.codewars.com/kata/count-odd-numbers-below-n/train/python

def odd_count(n):
    print(n)
    for i in range(n):
        if i % 2 != 0:
            print(i)
    pass
odd_count(10)