'''
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10.001st prime number?

@author: Dos
'''
import time
from primality_test import is_prime_Lucas_variation

def st_prime(n):
    i = 0
    stop = 0
    while stop < n:
        i += 1
        if is_prime_Lucas_variation(i):
            stop += 1
#             print(stop, i)
    
    return i



start_time = time.time()



print(st_prime(10001))


print(time.time() - start_time, "seconds")
