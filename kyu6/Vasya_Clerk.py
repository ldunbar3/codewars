# https://www.codewars.com/kata/vasya-clerk/train/python

'''
Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?
'''

def tickets(people):
    register_dict = {25: 0, 50: 0, 100: 0}

    for i in people:
        if i == 25:
            register_dict[25] += 1
        elif i == 50:
            if register_dict[25] >= 1:
                register_dict[50] += 1
                register_dict[25] -= 1
            else:
                return "NO"
        elif i == 100:
            if register_dict[50] >= 1 and register_dict[25] >= 1:
                register_dict[100] += 1
                register_dict[50] -= 1
                register_dict[25] -= 1
            elif register_dict[25] >= 3:
                register_dict[100] += 1
                register_dict[25] -= 3
            else:
                return "NO"
    return "YES"