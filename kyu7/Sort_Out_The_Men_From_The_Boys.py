# https://www.codewars.com/kata/sort-out-the-men-from-boys-1/train/python

def men_from_boys(arr):
    result = []
    for i in arr:
        if i not in result: result.append(i)
    men = sorted(list(filter(lambda x: x % 2 == 0, result)))
    boys = sorted(list(filter(lambda x: x % 2 != 0, result)), reverse = True)
    return men + boys