# https://www.codewars.com/kata/disemvowel-trolls/train/python

def disemvowel(string):
    nv = ""
    for i in string:
        if i not in 'aAeEiIoOuU':
            nv = nv + i

    return nv
