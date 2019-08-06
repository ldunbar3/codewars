# https://www.codewars.com/kata/string-incrementer/train/python

import re
def increment_string(s):
    number = re.findall(r'\d+', s)

    if number:
        ending_number = number[-1]
        s = s.rsplit(ending_number, 1)[0]
        number = str(int(ending_number) + 1)
        return s + '0' * (len(ending_number) - len(number)) + number
    return s + '1'