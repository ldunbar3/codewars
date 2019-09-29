# https://www.codewars.com/kata/find-me/train/python

def find_me(s):
    s = s.lower()
    if "me" in s:
        return s.find("me")
    else:
        return "i am not there"