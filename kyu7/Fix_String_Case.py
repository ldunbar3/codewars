# https://www.codewars.com/kata/5b180e9fedaa564a7000009a

'''
In this Kata, you will be given a string that may have mixed uppercase and
lowercase letters and your task is to convert that string to either lowercase
only or uppercase only based on:
'''

def solve(s):
    # lower = 0
    # upper = 0
    # for letter in s:
    #     if letter.islower():
    #         lower += 1
    #     elif letter.isupper():
    #         upper += 1
    # if lower >= upper:
    #     return s.lower()
    # else:
    #     return s.upper()

    return s.lower() if sum(1 for l in s if l.islower()) >= len(s) / 2 else s.upper()


print(solve("code"))#,"code")
print(solve("CODe"))#,"CODE")
print(solve("COde"))#,"code")
print(solve("Code"))#,"code")