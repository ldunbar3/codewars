# https://www.codewars.com/kata/add-commas-to-long-numbers/train/python

def add_commas(n):
    return f'{n:,}'

print(add_commas(5000000))