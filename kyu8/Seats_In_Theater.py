# https://www.codewars.com/kata/simple-fun-number-1-seats-in-theater/train/python

'''
Given the total number of rows and columns in the theater (nRows and nCols, respectively), and 
the row and column you're sitting in, return the number of people who sit strictly behind you and 
in your column or to the left, assuming all seats are occupied.
'''

def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_rows - row) * (tot_cols - col + 1)

