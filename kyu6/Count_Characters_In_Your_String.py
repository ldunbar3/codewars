# https://www.codewars.com/kata/count-characters-in-your-string/train/python

'''
The main idea is to count all the occuring characters(UTF-8) in string. If you have 
string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }
'''

def count(s):
    word_count = {}
    for key in s:
        if key not in word_count:
            word_count[key] = 1
        else:
            word_count[key] += 1
    return word_count



    # alphabet = dict( (key, 0) for key in string.ascii_lowercase )

    # for l in s:
    #     alphabet[l] += 1
    # print(alphabet)

    # return 

print(count('aba'))#, {'a': 2, 'b': 1})
print(count(''))#, {})