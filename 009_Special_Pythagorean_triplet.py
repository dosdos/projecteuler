'''
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

@author: Dos
'''
import time, math

M = 1000

# c = 1000 - a - b 
# b < 1000 - a - b 
# 2b < 1000 - a
# a < 1000 - 2b
# moreover a < b

def is_square(n):
    return int(math.sqrt(n)) ** 2 == n

def found_triplet(n):
    for a in range(1, int(n/3)):
        for b in range(a, int(n/2)):
            c = n - a - b
            if a * a + b * b == c * c:
                print("%d^2 + %d^2 = %d + %d = %d = %d^2" % (a, b, a * a, b * b, c * c, c))
                return a * b * c
    return 0


start_time = time.time()
print(found_triplet(M))
print(time.time() - start_time, "seconds")
# 
# start_time = time.time()
# 
# print(time.time() - start_time, "seconds")
