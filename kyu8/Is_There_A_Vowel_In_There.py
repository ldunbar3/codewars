# https://www.codewars.com/kata/is-there-a-vowel-in-there/train/python

def is_vow(inp):
    arr = []
    vowels = {97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}

    for i in inp:
        arr.append(vowels[i]) if i in vowels else arr.append(i)

    return arr