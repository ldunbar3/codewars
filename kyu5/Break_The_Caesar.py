# https://www.codewars.com/kata/break-the-caesar/train/python

'''
Given a message, your function must return the most likely shift value as an integer.
'''
import string 

def break_caesar(message):
    message = ''.join(x if x.isalpha() else ' ' for x in message).lower()
    analysis = []
    for shift in range(26):
        translation_table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[-shift:] + string.ascii_lowercase[:-shift])
        decoded_message = message.translate(translation_table)
        hits = 0
        for word in decoded_message.split():
            if word in WORDS:
                hits += 1
        analysis.append(hits)
    return analysis.index(max(analysis))