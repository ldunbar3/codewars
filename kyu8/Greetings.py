# https://www.codewars.com/kata/greetings-1/train/python

def greetings(time, name):
    if time and name:
        return f"Good {time} {name}"
    else:
        return "Hey dude greet someone"