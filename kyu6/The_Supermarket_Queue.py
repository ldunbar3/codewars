# https://www.codewars.com/kata/the-supermarket-queue/train/python
# https://en.wikipedia.org/wiki/Thread_pool <- READ THIS TO UNDERSTAND THREAD POOLING

'''
There is a queue for the self-checkout tills at the supermarket. Your task is
write a function to calculate the total time required for all the customers to
check out!

-> customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
-> n: a positive integer, the number of checkout tills.

The function should return an integer, the total time required.
'''

def queue_time(customers, n):
    tills = [0] * n
    for i in customers:
        tills[tills.index(min(tills))] += i
    return max(tills)

print(queue_time([], 1))#, 0, "wrong answer for case with an empty queue")
print(queue_time([5], 1))#, 5, "wrong answer for a single person in the queue")
print(queue_time([2], 5))#, 2, "wrong answer for a single person in the queue")
print(queue_time([1,2,3,4,5], 1))#, 15, "wrong answer for a single till")
print(queue_time([1,2,3,4,5], 100))#, 5, "wrong answer for a case with a large number of tills")
print(queue_time([1,2,3,4,5], 3))#, 7, "wrong answer for a case with a large number of tills")
print(queue_time([2,2,3,3,4,4], 2))#, 9, "wrong answer for a case with two tills")