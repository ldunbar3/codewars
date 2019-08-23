# https://www.codewars.com/kata/largest-5-digit-number-in-a-series/train/python

'''
Complete the solution so that it returns the greatest sequence of five consecutive
digits found within the number given. The number will be passed in as a string of
only digits. It should return a five digit integer. The number passed may be as large
as 1000 digits.
'''

def solution(digits):
    digits_array = list(str(digits))
    result = 0
    for i in range(0, len(digits_array) - 4):
        value = int(''.join(digits_array[i:i+5]))
        if value > result:
            result = value
    return result