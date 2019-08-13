# https://www.codewars.com/kata/do-i-get-a-bonus/train/python

def bonus_time(salary, bonus):
    return '${}'.format(salary*([1,10][bonus]))
