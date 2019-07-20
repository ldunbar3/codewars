# https://www.codewars.com/kata/backspaces-in-string/train/python

def clean_string(s):
    result = []
    for c in s:
        if c != '#':
            result.append(c)
        else:
            if c == '#':
                try:
                    result.pop()
                except:
                    pass
    return ''.join(result)