# https://www.codewars.com/kata/incrementer/train/python

def incrementer(nums):
    result = []
    count = 1
    for i in nums:
        result.append(int(str(i + count)[-1]))
        count += 1
    return result


print(incrementer([]))#, [])
print(incrementer([1, 2, 3]))#, [2, 4, 6])
print(incrementer([4, 6, 7, 1, 3]))#, [5, 8, 0, 5, 8])
print(incrementer([3, 6, 9, 8, 9]))#, [4, 8, 2, 2, 4])
print(incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]))#, [2, 4, 6, 8, 0, 2, 4, 6, 8, 9, 0, 1, 2, 2])

