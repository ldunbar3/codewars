# https://www.codewars.com/kata/adding-words-part-i/train/python

num_words = ['zero','one','two','three','four','five',
           'six','seven','eight','nine','ten','eleven',
           'twelve','thirteen','fourteen','fifteen','sixteen',
           'seventeen','eighteen','nineteen','twenty']

class Arith():
    def __init__(self, a):
        self.a = a
    def add(self, b):
        return num_words[num_words.index(self.a) + num_words.index(b)]