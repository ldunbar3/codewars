# https://www.codewars.com/kata/if-you-cant-sleep-just-count-sheep/train/python

def count_sheep(n):
    result = ""
    for i in range(1, n+1):
        #result = result + f"{i} sheep..."
        result += '{} {}'.format(i, "sheep...")
    return result

print(count_sheep(1))#, "1 sheep...");
print(count_sheep(2))#, "1 sheep...2 sheep...")
print(count_sheep(3))#, "1 sheep...2 sheep...3 sheep...")