'''
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

@author: Dos
'''
import time, math


NUM = 600851475143

# Fermat's factorization method

# FermatFactor(N): // N should be odd
# a ← ceil(sqrt(N))
# b2 ← a*a - N
# while b2 isn't a square:
#     a ← a + 1 // equivalently: b2 ← b2 + 2*a + 1
#     b2 ← a*a - N // a ← a + 1
# endwhile
# return a - sqrt(b2) // or a + sqrt(b2)


def is_square(n):
    return int(math.sqrt(n)) ** 2 == n


# Fermat primality test (it returns 1 if n is prime, a divisor otherwise)
def is_prime_fermat(n):
    a = int(math.ceil(math.sqrt(n)))
    b2 = a * a - n
    while not is_square(b2):
        a += 1
        b2 = a * a - n
    return a - math.sqrt(b2)

# print(is_prime_fermat(2639))


start_time = time.time()
found = False
factor = 2

while not found and factor < NUM:
    if (NUM % factor == 0) and (not factor % 2 == 0) and (is_prime_fermat(NUM/factor) == 1.0):
        found = True
        print("largest prime:", NUM/factor, "\nfactor:", factor)
    factor += 1


print("time:", time.time() - start_time, "seconds")



