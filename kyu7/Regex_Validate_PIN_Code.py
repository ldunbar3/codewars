# https://www.codewars.com/kata/regex-validate-pin-code/train/python

import re

def validate_pin(pin):
    if re.fullmatch("\d{4}|\d{6}", pin):
        return True
    else:
        return False
