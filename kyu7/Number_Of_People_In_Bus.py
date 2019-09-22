# https://www.codewars.com/kata/number-of-people-in-the-bus/python

def number(bus_stops):
    return sum(on - off for on, off in bus_stops)