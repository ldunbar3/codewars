# https://www.codewars.com/kata/sort-the-odd/python

def sort_array(source_array):

  odd_list = []
  sorted_list = []
  # create a list of odd items
  for i in source_array:
    if i % 2 != 0:
      odd_list.append(i)
  # reverse sort it so we can pop() it later
  odd_list.sort(reverse=True)

  # iterate through source_array
  for i in source_array:
    if i % 2 == 0:
      # append current even item to sorted_list
      sorted_list.append(i)
    elif i % 2 != 0:
      #pop() off the last item in odd_list and append it to sorted_list
      sorted_list.append(odd_list.pop())

  return sorted_list