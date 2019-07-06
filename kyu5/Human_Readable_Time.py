# https://www.codewars.com/kata/human-readable-time/train/python

def make_readable(seconds):
  m, s = divmod(seconds, 60)
  h, m = divmod(m, 60)
  return f"{h:02d}:{m:02d}:{s:02d}"