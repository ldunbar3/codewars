# https://www.codewars.com/kata/autocomplete-yay/train/python

'''
The autocomplete function will take in an input string and a dictionary array and 
return the values from the dictionary that start with the input string. If there are more than 
5 matches, restrict your output to the first 5 results. If there are no matches, return an empty array.
'''

def autocomplete(input_, dictionary):
    input_ = ''.join(c for c in input_ if c.isalpha())
    return filter(lambda c:c.lower().startswith(input_.lower()), dictionary)[:5]