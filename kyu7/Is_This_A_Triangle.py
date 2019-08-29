# https://www.codewars.com/kata/is-this-a-triangle/train/python

def is_triangle(a, b, c):
    tri = sorted([a,b,c])
    return tri[0] + tri[1] > tri[2]