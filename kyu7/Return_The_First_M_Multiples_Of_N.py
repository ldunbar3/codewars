# https://www.codewars.com/kata/return-the-first-m-multiples-of-n/train/python

def multiples(m, n):
    result=[]
    for i in range (1, m+1) :
        result.append(i*n)
    return result