# https://www.codewars.com/kata/558ee8415872565824000007

def is_divisible(n, *args):
    return all(map(lambda i: n % i == 0, args))