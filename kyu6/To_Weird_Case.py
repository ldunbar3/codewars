# https://www.codewars.com/kata/weird-string-case/train/python

'''
Note: The instructions are not very clear on this one, and I 
wasted a lot of time just trying to figure out what was expected. 
The goal is to alternate the case on *EACH WORD* of the string,
with the first letter being uppercase. You will not pass all of the 
tests if you alternate case based on the indexes of the entire string
as a whole.

eg. "This is a test string" should return "ThIs Is A TeSt StRiNg"
                                           ^ ^  ^  ^ ^ ^  ^ ^ ^
'''

def to_weird_case(string):
  starter = string.split()
  result = ""
  for index, char in enumerate(starter):
    for i, c in enumerate(char):
      if i == 0 or i % 2 == 0:
        result = result + (c.upper())
      else:
        result = result + (c.lower())
    result = result + " "
  return result.rstrip()