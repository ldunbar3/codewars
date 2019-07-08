# https://www.codewars.com/kata/isograms/train/python

def is_isogram(string):
  return True if len(set(list(string.upper()))) == len(list(string.upper())) else False