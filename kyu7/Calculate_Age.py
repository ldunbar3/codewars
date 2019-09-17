# https://www.codewars.com/kata/calculate-two-peoples-individual-ages/train/python

'''
Create a function that takes in the sum and age difference of two people, calculates their 
individual ages, and returns a pair of values if those exist or an empty values if:
    sum < 0
    difference < 0
    Either of the calculated ages come out to be negative
'''

def get_ages(sum_, difference):
    a = (sum_ + difference) / 2
    b = sum_ - a
    return None if sum_ < 0 or difference < 0 or a < 0 or b < 0 else (max(a,b), min(a,b))