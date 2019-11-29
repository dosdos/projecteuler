"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

@author: Dos
"""
import time

N = 100000000


start_time = time.time()
acc = 0
for i in range(0, N):
    if i % 3 == 0 or i % 5 == 0:
        acc += i
print(acc)
print(time.time() - start_time, "seconds")


start_time = time.time()
acc = 0
for i in filter(lambda x: x % 3 == 0 or x % 5 == 0, range(0, N)):
    acc += i
print(acc)
print(time.time() - start_time, "seconds")


# Look at generator expressions there: http://www.python.org/dev/peps/pep-0289/#id8
# Generator expressions as a high performance, memory efficient generalization of list comprehensions and generators
start_time = time.time()
acc = sum(x for x in range(0, N) if x % 3 == 0 or x % 5 == 0)
print(acc)
print(time.time() - start_time, "seconds")


# with list comprehensions
start_time = time.time()
acc = sum([x for x in range(0, N) if x % 3 == 0 or x % 5 == 0])
print(acc)
print(time.time() - start_time, "seconds")


# with lambda
start_time = time.time()
acc = sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(0, N)))
print(acc)
print(time.time() - start_time, "seconds")

# skip useless number
start_time = time.time()
acc = 0
for i in range(3, N, 3):
    acc += i
for i in range(5, N, 5):
    if not i % 3 == 0:
        acc += i
print(acc)
print(time.time() - start_time, "seconds")


def get_summation(multiplier, ceiling):
    return multiplier * sum(range(((ceiling-1) // multiplier) + 1))


def get_fast_summation(multiplier, ceiling):
    div = (ceiling-1) // multiplier
    return multiplier * (div * (div+1) // 2)


# use summations
start_time = time.time()
print(get_summation(3, N) + get_summation(5, N) - get_summation(15, N))
print(time.time() - start_time, "seconds")

# use fast summations
start_time = time.time()
print(get_fast_summation(3, N) + get_fast_summation(5, N) - get_fast_summation(15, N))
print(time.time() - start_time, "seconds")
