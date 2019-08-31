# https://www.codewars.com/kata/convert-string-to-camel-case/train/python

'''
Complete the method/function so that it converts dash/underscore delimited words into 
camel casing. The first word within the output should be capitalized only if the original 
word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
'''

def to_camel_case(text):
    result = ""
    text = text.replace('_', '-')
    for k, v in enumerate(text.split('-')):
        result += v if k == 0 else v.capitalize() # ternary
    return result