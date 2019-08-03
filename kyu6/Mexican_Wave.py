# https://www.codewars.com/kata/mexican-wave/train/python

def wave(str):
    result = []
    for key, val in enumerate(str):
        if val.isalpha():
            result.append(str[:key] + str[key].upper() + str[key+1:])
            # result.append(f"{str[:key]}{str[key].upper()}{str[key+1:]}") <- works in my environment, not on codewars

    return result

print(wave("This has spaces"))