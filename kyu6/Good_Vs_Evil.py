# https://www.codewars.com/kata/good-vs-evil/train/python

'''
Although weather, location, supplies and valor play a part in any battle,
if you add up the worth of the side of good and compare it with the worth of
 the side of evil, the side with the larger worth will tend to win.

Thus, given the count of each of the races on the side of good, followed by
the count of each of the races on the side of evil, determine which side wins.
'''

def goodVsEvil(good, evil):
    good = list(map(int, good.split(" ")))
    evil = list(map(int, evil.split(" ")))

    good_scores = [1,2,3,3,4,10]
    evil_scores = [1,2,2,2,3,5,10]

    good_result = sum(list(x * y for x, y in zip(good, good_scores)))
    evil_result = sum(list(x * y for x, y in zip(evil, evil_scores)))

    if good_result > evil_result:
        return "Battle Result: Good triumphs over Evil"
    elif good_result < evil_result:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"