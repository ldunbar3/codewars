# https://www.codewars.com/kata/the-office-i-outed/train/python

def outed(meet, boss):
  anger = 0
  for k, v in meet.items():
    if k == boss: anger += v
    anger += v
  return "Get Out Now!" if anger / len(meet) <= 5 else "Nice Work Champ!"