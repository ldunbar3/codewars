# https://www.codewars.com/kata/string-ends-with/train/python

def solution(string, ending):

    # print(string[-len(ending):])
    # if string[-len(ending):] == ending:
    #     return True

    return True if string[-len(ending):] == ending else False





print(solution('abcde', 'cde'))#, True)
print(solution('abcde', 'abc'))#, False)