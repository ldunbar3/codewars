# https://www.codewars.com/kata/see-you-next-happy-year/train/python

def next_happy_year(year):
    while True:
        year += 1
        if len(set(list(str(year)))) == 4:
            return year
            break