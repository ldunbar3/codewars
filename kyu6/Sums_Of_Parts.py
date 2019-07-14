# https://preview.codewars.com/kata/sums-of-parts/train/python

def parts_sums(ls):
    result = []
    total = sum(ls)
    result.append(total)
    for i in ls:
        total = total - i
        result.append(total)
    return result