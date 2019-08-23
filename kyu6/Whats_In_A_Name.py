# https://www.codewars.com/kata/whats-in-a-name/train/python

'''
Test whether or not the string contains all of the letters which spell a given name, in order.
'''

def name_in_str(str, name):
    index = 0
    result = []
    for n in list(name.lower()):
        location = str.lower().find(n, index, len(str))
        if location != -1:
            result.append(location)
            index = location + 1
    return len(result) == len(name)