# https://www.codewars.com/kata/shortest-word/train/python

def find_short(s):
    min_word = []
    for item in s.split(" "):
        min_word.append(len(item))
    return min(min_word)