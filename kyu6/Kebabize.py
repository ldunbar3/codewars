# https://preview.codewars.com/kata/kebabize/train/python

def kebabize(string):

    result = ''
    for char in string:
        if char.isalpha():
            if char.isupper():
                result += '-' + char.lower()
            else:
                result += char
    if len(result) > 0:
        return result if result[0] != '-' else result[1:]
    else:
        return ''

