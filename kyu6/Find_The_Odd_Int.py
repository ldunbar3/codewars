# https://www.codewars.com/kata/find-the-odd-int/train/python

def find_it(seq):
    for i in list(set(seq)):
        if seq.count(i) % 2 != 0:
            return i

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))#, 5)
