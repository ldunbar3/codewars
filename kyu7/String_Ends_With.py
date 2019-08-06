# https://www.codewars.com/kata/string-ends-with/train/python

def solution(string, ending):
    return True if string[-len(ending):] == ending else False