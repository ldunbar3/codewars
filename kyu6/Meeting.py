# https://www.codewars.com/kata/meeting/train/python

def meeting(s):
    result = []
    for p in s.split(';'):
        first, last = p.split(':')
        result.append(f"({last.upper()}, {first.upper()})")
    return ''.join(sorted(result))