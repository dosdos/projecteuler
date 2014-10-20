import math
import random
import time


def is_square(n):
    """ Square test.
    
    Args
        n: an integer number to test
    Returns
        True if n is a square, False otherwise.
    """
    return int(math.sqrt(n)) ** 2 == n


def prime_factors(n):
    """ Get the list of factors (greater than 1) of an integer number.
    
    Args
        n: an integer number
    Returns
        The list of all integer factors ordered by smallest to greatest (factors
        that occurs multiple times are repeated).
    """
    factors = []  
    
    # iterate from 2 to n/2
    for i in range(2, int(n / 2) + 1):
        # while n is divisible by i 
        while n % i == 0:
            # add i to factors
            factors.append(i)
            # and decrease n
            n = int(n / i)
    # if n has no factors (it's a prime)
    if len(factors) == 0:
        # add it to factors
        factors.append(n)
    return factors


def is_prime_trial_division(n):
    """ Trivial primality test. A number is prime if it has no divisors other
    than itself and one, so try with iterative divisions.
    
    Args
        n: an integer number to test
    Returns
        True if n is prime, False otherwise.
    """
    # Base case: n = 1 | n = 2
    if n == 1 or n == 2:
        return False
    
    # iterate from 2 to n/2
    i = 2
    while i < int(n / 2) + 1:
        # check if n is divisible by i
        if n % i == 0:
            return False
        i += 1
    
    # return test result
    return True


def is_prime_trial_division_opt(n):
    """ Trivial primality test. A number is prime if it has no divisors other
    than itself and one, so try with iterative divisions.
    
    Args
        n: an integer number to test
    Returns
        True if n is prime, False otherwise.
    """
    # Base case: n = 1 | n = 2 | n == 3 | n%2 = 0 | n%3 == 0
    if n == 1 or n == 2 or n == 3 or n%2 == 0 or n%3 == 0:
        return False
    
    # iterate from 2 to n/2
    i = 2
    while i < int(n / 2) + 1:
        # check if n is divisible by i
        if n % i == 0:
            return False
        i += 1
    
    # return test result
    return True


def is_prime_fermat(n):
    """ Fermat primality test.
    
    Args
        n: an integer number to test
    Returns
        True if n is prime, False otherwise.
    """
    # Base case: n = 1 | n = 2 | n == 3 | n%2 = 0 | n%3 == 0
    if n == 1 or n == 2 or n == 3 or n%2 == 0 or n%3 == 0:
        return False
    
    # Iterative case: apply Fermat method
    a = int(math.ceil(math.sqrt(n)))
    b2 = a * a - n
    while not is_square(b2):
        a += 1
        b2 = a * a - n
    
    # return test result
    return a - math.sqrt(b2) == 1.


def is_prime_Lucas_variation(n):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0: 
        return False
    elif n < 9:
        return True
    elif n % 3 == 0: 
        return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0: 
            return False
        else:
            f += 6
    return True


def miller_rabin_test(a, i, n):
    """ Miller-Rabin pseudo-primality test. Does not test prime 2!
    
    Example call: miller_rabin_test(random.randint(2, n - 2), n - 1, n)
    
    Args
        a: a random integer
        i: usually i = n - 1
        n: the integer number to test
    Returns
        1 if n is prime
    """
    # Base case: n = 1 | n = 2 | n == 3 | n%2 = 0 | n%3 == 0
    if n == 1 or n == 2 or n == 3 or n%2 == 0 or n%3 == 0:
        return 0
    
    if i == 0:
        return 1
    x = miller_rabin_test(a, i // 2, n)
    if x == 0:
        return 0
    y = (x * x) % n
    if ((y == 1) and (x != 1) and (x != (n - 1))):
        return 0
    if (i % 2) != 0:
        y = (a * y) % n
    return y

def is_prime_Miller_Rabin(n):
    return miller_rabin_test(random.randint(2, n - 2), n - 1, n) == 1


#===============================================================================
# TEST - is_prime
#===============================================================================

def is_prime_test():
    # 561 - the smallest Carmichael number
    print("\n")
    start_time = time.time()
    print("is_prime_trials(561):\t", "\t\t", is_prime_trial_division(561), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_trials2(561):\t", "\t\t", is_prime_trial_division_opt(561), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_fermat(561):\t", "\t\t", is_prime_fermat(561), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_Lucas(561):\t", "\t\t", is_prime_Lucas_variation(561), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_M-R(561):\t", "\t\t", is_prime_Miller_Rabin(561), "\t", (time.time() - start_time)*1000, "milliseconds")
    
    # 5394826801 - the fifth Carmichael number
    print("\n")
    start_time = time.time()
    print("is_prime_trials(5394826801):", "\t\t", is_prime_trial_division(5394826801), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_trials2(5394826801):", "\t\t", is_prime_trial_division_opt(5394826801), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_fermat(5394826801):", "\t\t", is_prime_fermat(5394826801), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_Lucas(5394826801):", "\t\t", is_prime_Lucas_variation(5394826801), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_M-R(5394826801):", "\t\t", is_prime_Miller_Rabin(5394826801), "\t", (time.time() - start_time)*1000, "milliseconds")
    
    # 9746347772161 - the ninth Carmichael number
    print("\n")
    start_time = time.time()
    print("is_prime_trials(9746347772161):", "\t", is_prime_trial_division(9746347772161), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_trials2(9746347772161):", "\t", is_prime_trial_division_opt(9746347772161), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_fermat(9746347772161):", "\t", is_prime_fermat(9746347772161), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_Lucas(9746347772161):\t", "\t", is_prime_Lucas_variation(9746347772161), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_M-R(9746347772161):\t", "\t", is_prime_Miller_Rabin(9746347772161), "\t", (time.time() - start_time)*1000, "milliseconds")
    
    # 1299827 - the 100008th prime
    print("\n")
    start_time = time.time()
    print("is_prime_trials(1299827):", "\t\t", is_prime_trial_division(1299827), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_trials2(1299827):", "\t\t", is_prime_trial_division_opt(1299827), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_fermat(1299827):", "\t\t", is_prime_fermat(1299827), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_Lucas(1299827):", "\t\t", is_prime_Lucas_variation(1299827), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_M-R(1299827):\t", "\t\t", is_prime_Miller_Rabin(1299827), "\t", (time.time() - start_time)*1000, "milliseconds")
    
    # 140737488355327 = 2351 x 4513 x 13264529
    print("\n")
    start_time = time.time()
    print("is_prime_trials(140737488355327):", "\t", is_prime_trial_division(140737488355327), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_trials2(140737488355327):", "\t", is_prime_trial_division_opt(140737488355327), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_fermat(140737488355327):", "\t", is_prime_fermat(140737488355327), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_Lucas(140737488355327):", "\t", is_prime_Lucas_variation(140737488355327), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_M-R(140737488355327):", "\t\t", is_prime_Miller_Rabin(140737488355327), "\t", (time.time() - start_time)*1000, "milliseconds")
    
    # 122949823 is prime!
    print("\n")
    start_time = time.time()
    print("is_prime_Lucas(122949823):", "\t\t", is_prime_Lucas_variation(122949823), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_M-R(122949823):", "\t\t", is_prime_Miller_Rabin(122949823), "\t", (time.time() - start_time)*1000, "milliseconds")
    
    # 472882027 is prime!
    print("\n")
    start_time = time.time()
    print("is_prime_Lucas(472882027):", "\t\t", is_prime_Lucas_variation(472882027), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_M-R(472882027):", "\t\t", is_prime_Miller_Rabin(472882027), "\t", (time.time() - start_time)*1000, "milliseconds")
    
    # 982451653 is prime!
    print("\n")
    start_time = time.time()
    print("is_prime_Lucas(982451653):", "\t\t", is_prime_Lucas_variation(982451653), "\t", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("is_prime_M-R(982451653):", "\t\t", is_prime_Miller_Rabin(982451653), "\t", (time.time() - start_time)*1000, "milliseconds")


#===============================================================================
# TEST - print primes lower than n
#===============================================================================

def print_primes(n):
    start_time = time.time()
    print("trials:", "\t\t", [x for x in range(4,n) if is_prime_trial_division(x)], "\n", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("trials2:", "\t\t", [x for x in range(4,n) if is_prime_trial_division_opt(x)], "\n", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("fermat:", "\t\t", [x for x in range(4,n) if is_prime_fermat(x)], "\n", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("Lucas:", "\t\t\t", [x for x in range(4,n) if is_prime_Lucas_variation(x)], "\n", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("M-R:", "\t\t\t", [x for x in range(4,n) if is_prime_Miller_Rabin(x)], "\n", (time.time() - start_time)*1000, "milliseconds")

def print_primes_len(n):
#     start_time = time.time()
#     print("trials:", "\t\t", len([x for x in range(4,n) if is_prime_trial_division(x)]), "\n", (time.time() - start_time)*1000, "milliseconds")
#     start_time = time.time()
#     print("trials2:", "\t\t", len([x for x in range(4,n) if is_prime_trial_division_opt(x)]), "\n", (time.time() - start_time)*1000, "milliseconds")
#     start_time = time.time()
#     print("fermat:", "\t\t", len([x for x in range(4,n) if is_prime_fermat(x)]), "\n", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("Lucas:", "\t\t\t", len([x for x in range(4,n) if is_prime_Lucas_variation(x)]), "\n", (time.time() - start_time)*1000, "milliseconds")
    start_time = time.time()
    print("M-R:", "\t\t\t", len([x for x in range(4,n) if is_prime_Miller_Rabin(x)]), "\n", (time.time() - start_time)*1000, "milliseconds")


#===============================================================================
# MAIN
#===============================================================================

# is_prime_test()
# print_primes(1000000)
# print_primes_len(1000000)
# print(prime_factors(276))
