# https://www.codewars.com/kata/sum-of-a-beach/train/python

import re

def sum_of_a_beach(beach):
    wordlist = ["sand", "water", "fish", "sun"]
    return len(re.findall(r"(?=("+'|'.join(wordlist)+r"))", beach.lower()))