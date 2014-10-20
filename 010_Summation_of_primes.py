'''
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

@author: Dos
'''
import time
from primality_test import is_prime_Lucas_variation

def find_sum(n):
    s = 0
    for i in range(1,n+1):
        if is_prime_Lucas_variation(i):
            s += i
    return s


start_time = time.time()
print(find_sum(2000000))
print(time.time() - start_time, "seconds")

