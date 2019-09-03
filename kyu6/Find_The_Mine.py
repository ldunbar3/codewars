# https://www.codewars.com/kata/find-the-mine/train/python

'''
Write a function mineLocation/MineLocation that accepts a 2D array, and returns 
the location of the mine. The mine is represented as the integer 1 in the 2D array. 
Areas in the 2D array that are not the mine will be represented as 0s. 
'''

def mineLocation(field):
    for x, v in enumerate(field):
        for y, z in enumerate(v):
            if z == 1:
                return [x,y]