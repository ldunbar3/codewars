# https://www.codewars.com/kata/are-you-playing-banjo/train/python

'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!
'''

def areYouPlayingBanjo(name):
    if name[0] in ["R", "r"]:
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"