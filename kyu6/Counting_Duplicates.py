# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    result = []
    text = text.upper()
    for i in text:
        if text.count(i) > 1 and i not in result:
            result.append(i)
    return len(result)