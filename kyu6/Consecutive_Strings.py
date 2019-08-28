# https://www.codewars.com/kata/56a5d994ac971f1ac500003e

'''
You are given an array strarr of strings and an integer k. Your task is
to return the first longest string consisting of k consecutive strings taken in the array.
'''
def longest_consec(strarr, k):
    to_beat = ""
    if k >= 0:
        for i in range(len(strarr)):
            while i <= len(strarr)-k:
                current_string = ''.join(strarr[i:i+k])
                if len(current_string) > len(to_beat):
                    to_beat = current_string
                break
    else:
        return to_beat
    return to_beat