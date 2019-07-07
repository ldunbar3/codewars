# https://www.codewars.com/kata/unique-in-order/train/python

def unique_in_order(iterable):
  array = []
  for i, v in enumerate(iterable):
      if (i == 0 or v != array[-1]): array.append(v)

  return array