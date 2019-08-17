# https://www.codewars.com/kata/who-likes-it/train/python

def likes(names):
    total_likes = len(names)

    if total_likes == 0:
        return "no one likes this"
    elif total_likes == 1:
        return f"{names[0]} likes this"
    elif total_likes == 2:
        return f"{names[0]} and {names[1]} like this"
    elif total_likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif total_likes > 3:
        return  f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


print(likes([]))#, 'no one likes this')
print(likes(['Peter']))#, 'Peter likes this')
print(likes(['Jacob', 'Alex']))#, 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']))#, 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))#, 'Alex, Jacob and 2 others like this')