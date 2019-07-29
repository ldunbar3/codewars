# https://www.codewars.com/kata/which-string-is-worth-more/train/python

def highest_value(a,b):
    atotal, btotal = 0, 0

    for achar in set(list(a)):
        atotal += ord(achar)

    for bchar in set(list(b)):
        btotal += ord(bchar)

    return a if atotal >= btotal else b