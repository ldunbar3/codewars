# https://preview.codewars.com/kata/sums-of-parts/train/python

def parts_sums(ls):
    result = [sum(ls)]
    total = sum(ls)
    for i in ls:
        total = total - i
        result.append(total)
    return result