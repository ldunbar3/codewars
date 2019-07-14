# https://www.codewars.com/kata/word-a10n-abbreviation/train/python

import re

def abbreviate(s):
    a = lambda word: word[0] + str(len(word)-2) + word[-1] if len(word) > 3 else word
    regex = re.split("([^a-zA-Z])", s)
    result = map(a, regex)
    return "".join(result)