# https://www.codewars.com/kata/directions-reduction/train/python

'''
Write a function dirReduc which will take an array of strings and returns an array of strings
with the needless directions removed (W<->E or S<->N side by side).
'''
def dirReduc(arr):
    cancelled_dict = {"NORTH" : "SOUTH", "SOUTH" : "NORTH" , "EAST" : "WEST" , "WEST" : "EAST"}
    result = []
    for i in arr:
        print(i)
        if result and cancelled_dict[i] == result[-1]:
            print(f"Result Array: {result}, Match: {cancelled_dict[i]}, Last one in Result Array: {result[-1]}")
            result.pop()
        else:
            result.append(i)
    return result