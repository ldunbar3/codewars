# https://www.codewars.com/kata/find-duplicates/train/python

def duplicates(array):
    dupes = []
    for i in range(len(array)):
        if array[i] in array[:i] and array[i] not in dupes:
            dupes.append(array[i])
    return dupes