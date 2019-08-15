# https://www.codewars.com/kata/grouped-by-commas/train/python

'''
Finish the solution so that it takes an input n (integer) and returns a string that
is the decimal representation of the number grouped by commas after every 3 digits.
'''

def group_by_commas(n):
    return '{:,}'.format(n)

    # would work if kata used later python version -
    # return f"{n:,d}"