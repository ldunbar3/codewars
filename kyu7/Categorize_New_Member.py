# https://www.codewars.com/kata/categorize-new-member/train/python

'''
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would 
like your help with an application form that will tell prospective members which category they 
will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this 
croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input will consist of a list of lists containing two items each. Each list contains information for 
a single potential member. Information consists of an integer for the person's age and an integer for 
the person's handicap.
'''

def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]