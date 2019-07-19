# https://www.codewars.com/kata/exes-and-ohs/train/python

def xo(s):
    return s.lower().count('x') == s.lower().count('o')





print(xo('zp'))
print(xo('xo0'))
print(xo('XXXoOo'))