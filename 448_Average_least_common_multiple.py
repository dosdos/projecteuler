'''
Average least common multiple

The function lcm(a,b) denotes the least common multiple of a and b.
Let A(n) be the average of the values of lcm(n,i) for 1<=i<=n.
E.g: A(2)=(2+2)/2=2 and A(10)=(10+10+30+20+10+30+70+40+90+10)/10=32.

Let S(n) = SUM A(k) for 1<=k<=n.
S(100)=122726.
Find S(99999999019) mod 999999017.

@author: Dos
'''
import time, functools


def prime_factors(n):
    """ Get the list of factors (greater than 1) of an integer number.
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

def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return functools.reduce(gcd, numbers)

def lcm(*numbers):
    """Return lowest common multiple."""    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return functools.reduce(lcm, numbers, 1)

def avg(numbers):
    return sum(numbers) / len(numbers)

def A1(n):
    return avg([lcm(i,n) for i in range(1, n + 1)])

def A2(n):
    factors = prime_factors(n)
    tot_sum = 0
    for i in range(1, n + 1):
        for f in factors:
            if i % f == 0: i /= f
        tot_sum += i
    return tot_sum

def S1(n):
    s = 0
    for i in range(1,n+1):
        s += A1(i)
    return s

def S2(n):
    s = 0
    for i in range(1,n+1):
        s += A2(i)
    return s


print('avg: ',avg([2,3,4]))
print('gdc: ',gcd(8,24,6))
print('lcm: ',lcm(2,3,5,24,6))
print('A1(2): ',A1(2))
print('A1(10): ',A1(10))
print('A2(2): ',A2(2))
print('A2(10): ',A2(10))


start_time = time.time()
print('S2(100): ',S2(1000))
print(time.time() - start_time, "seconds")

# start_time = time.time()
# print('S1(100): ',S1(100))
# print(time.time() - start_time, "seconds")


# NB: 99999999019 % 999999017 = 97319
# NB: 99999999019 / 999999017 = 100.00009731909566
