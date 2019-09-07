# https://www.codewars.com/kata/find-the-vowels/train/python

def vowel_indices(word):
    result = []
    for k, v in enumerate(word.lower()):
        if v in 'aeiouy':
            result.append(k+1)
    return result