# https://www.codewars.com/kata/character-limits-how-long-is-your-piece-of-string/train/python

def charCheck(text, max, spaces):
    if spaces == False:
        text = text.replace(" ", "")
    return [len(text) <= max, text[0:max]]