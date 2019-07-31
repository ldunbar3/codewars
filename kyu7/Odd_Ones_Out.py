# https://www.codewars.com/kata/odd-ones-out/train/python

def odd_ones_out(numbers):
    results = []
    for item in numbers:
        if numbers.count(item) % 2 != 1:
            results.append(item)
    return results