# https://www.codewars.com/kata/where-my-anagrams-at/train/python

'''
The instructions don't mention this, but your return list must maintain the same order
of list items as the list that was passed into the function.
'''

def anagrams(word, wordlist):
  word_dict = {}
  result = []

  for char in list(word):
    word_dict[char] = word.count(char)

  for item in wordlist:
    wordlist_dict = {}
    for l in item:
      wordlist_dict[l] = item.count(l)
    if wordlist_dict == word_dict:
      result.append(item)

  return result