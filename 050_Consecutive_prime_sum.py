'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

@author: Dos
'''
import time, math

K = 1000
M = 1000000

def is_square(n):
    return int(math.sqrt(n)) ** 2 == n

def is_prime_fermat(n):
    """ Fermat primality test.
    
    Args
        n: an integer number to test
    Returns
        True if n is prime, False otherwise.
    """
    r = False
    
    # Base case n = 1
    if n == 1:
        r = True
    # Base case n = 2
    elif n == 2:
        r = True
    # Base case n is even
    elif n%2 == 0:
        r = False
    # Iterative case: apply Fermat method
    else:
        a = int(math.ceil(math.sqrt(n)))
        b2 = a * a - n
        while not is_square(b2):
            a += 1
            b2 = a * a - n
        r = a - math.sqrt(b2) == 1.
    
    # return test result
    return r

start_time = time.time()


l = 101

p = [i for i in range(l) if is_prime_fermat(i)]

max_len = 0

for i in range(len(p)):
    s = 0
    j = i
    while j < len(p):
        if s in p:
            max_len = j - i
            print('i =', i, ' j =', j, ' p[i] =', p[i], ' p[j] =', p[j], ' s =', s, ' max_len =', max_len, 'trovato!')
        else:
            print('i =', i, ' j =', j, ' p[i] =', p[i], ' p[j] =', p[j], ' s =', s, ' max_len =', max_len)
        s = p[i] + p [j]
        j += 1
            
        

print(p, max_len)


# found = False
# i = M
# 
# # for i in range(4,10):
# while not found and i>1:
#     if is_prime_fermat(i)==1:
#         found = True
#         print(i)
#     i -= 1


# for i in range(1000):
#     if is_prime_fermat(i)==1:
#         print(i)

print(time.time() - start_time, "seconds")
