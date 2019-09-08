#

def DNA_strand(dna):
    result  = ""
    for x in dna:
        if x == 'A':
            result += 'T'
        if x == 'T':
            result += 'A'
        if x == 'C':
            result += 'G'
        if x == 'G':
            result += 'C'
    return result