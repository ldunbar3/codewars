# https://www.codewars.com/kata/persistent-bugger/train/python

def persistence(n):
  count = 0
  tempN = [int(d) for d in str(n)]
  print("Original List: " + str(tempN))

  while len(tempN) > 1:
    product = 1
    for x in tempN:
      product *= x
    print("Product: " + str(product))
    tempN = [int(d) for d in str(product)]
    print("Split items: " + str(tempN))  
    count += 1
  return count

print(persistence(39))
