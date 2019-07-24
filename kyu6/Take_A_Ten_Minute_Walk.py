# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def isValidWalk(walk):
    x = 0
    y = 0
    for i in walk:
        if len(walk) != 10:
            return False
            break
        elif i == 'n':
            y += 1
        elif i == 's':
            y -= 1
        elif i == 'e':
            x += 1
        elif i == 'w':
            x -= 1
    if x == y == 0:
        return True
    else:
        return False