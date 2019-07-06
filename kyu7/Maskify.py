# https://www.codewars.com/kata/credit-card-mask/train/python

def maskify(cc):
  return "#" * int(len(cc) - 4) + cc[-4::1]