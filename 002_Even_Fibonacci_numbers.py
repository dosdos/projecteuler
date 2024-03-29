'''
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

@author: Dos
'''
import time
N = 4000000

def fibonacci(n):
    cur, prev, acc, tmp = 1, 0 , 0, 0
    
    while cur < n:
        if cur % 2 == 0:
            acc += cur
        tmp = prev + cur
        prev = cur
        cur = tmp
    
    return acc


start_time = time.time()
print('%desimo numero di Fibonacci: %d' % (N, fibonacci(N)))
print(time.time() - start_time, "seconds")


