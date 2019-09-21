# https://www.codewars.com/kata/transportation-on-vacation/train/python

'''
Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. 
Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).
'''

def rental_car_cost(days):
    rate = 40
    discount = 0
    if days >= 7:
        discount = 50
    elif days >= 3:
        discount = 20
    return days * rate - discount



print(rental_car_cost(1))#,40)
print(rental_car_cost(4))#,140)
print(rental_car_cost(7))#,230)
print(rental_car_cost(8))#,270)