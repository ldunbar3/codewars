# https://www.codewars.com/kata/highest-scoring-word/train/python

import string

def high(x):
    word_scores = {}
    alphabet = dict( (key, string.ascii_lowercase.find(key)+1) for key in string.ascii_lowercase )
    s = x.lower().split(" ")
    for word in s:
        current_score = 0
        for c in word:
            current_score = current_score + alphabet[c]
        word_scores[word] = current_score
    return max(word_scores, key=word_scores.get)