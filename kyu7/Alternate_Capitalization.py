# https://www.codewars.com/kata/alternate-capitalization/train/python

def capitalize(s):
    result = ""
    for k, v in enumerate(s):
        if k == 0 or k % 2 == 0:
            result += v.upper()
        else:
            result += v.lower()
    return [result, result.swapcase()]