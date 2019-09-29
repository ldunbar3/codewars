# https://www.codewars.com/kata/find-me/train/python

def find_me(s):
    r = s.lower().find('me')
    if r == -1:
        return "i am not there"
    return r