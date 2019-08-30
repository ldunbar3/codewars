# https://www.codewars.com/kata/land-perimeter/train/python

'''
Given an array of strings complete the function landPerimeter by calculating 
the total perimeter of all the islands. Each piece of land will be marked with 'X' while the 
water fields are represented as 'O'. Consider each tile being a perfect 1 x 1piece of land. 
'''

def land_perimeter(array):
    perimeter = 0
    for r in range(len(array)):
        for c in range(len(array[r])):
            if array[r][c] == 'X':
                perimeter += 4
                #print(f"Gridpoint: {r,c}, Perimeter: {perimeter}")
                if c > 0 and array[r][c-1] == 'X':
                    perimeter -= 2
                if r >= 1 and array[r-1][c] == 'X':
                    perimeter -= 2

    return f"Total land perimeter: {perimeter}"

# print(land_perimeter(['XXXXXXXXX'])) # 20
# print(land_perimeter(['XXXXX', 'XXXXX', 'OOOOO', 'OOOOO', 'OOOOO'])) # 14
print(land_perimeter(['XOOXO', 'XOOXO', 'OOOXO', 'OOOXO', 'XXXOO'])) # 24
# print(land_perimeter(['XOOXO', 'XOOXO', 'OOOXO', 'XXOXO', 'OXOOO']))  # 24
# print(land_perimeter(['XOOOO', 'XOOOO', 'XOOOO', 'OOOOO', 'OOOOO'])) # 8
# print(land_perimeter(['XOO', 'XOO', 'OXO'])) # 10
# print(land_perimeter(['XOO', 'XXO'])) # 8
# print(land_perimeter(['XOOOO', 'XOOOO', 'XOOOO', 'XOOOO', 'XOOOO'])) # 12
