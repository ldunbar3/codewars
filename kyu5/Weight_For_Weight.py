# https://www.codewars.com/kata/55c6126177c9441a570000cc

def order_weight(strng):
    return ' '.join(c[1] for c in sorted((sum(int(b) for b in a), a) for a in strng.split()))