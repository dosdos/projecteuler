'''
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

@author: Dos
'''
import time


start_time = time.time()
acc = 0
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        acc += i
print(acc)
print(time.time() - start_time, "seconds")


start_time = time.time()
acc = 0
for i in filter(lambda x: x % 3 == 0 or x % 5 == 0, range(0, 1000)):
    acc += i
print(acc)
print(time.time() - start_time, "seconds")


# Look at generator expressions there: http://www.python.org/dev/peps/pep-0289/#id8
# Generator expressions as a high performance, memory efficient generalization of list comprehensions [1] and generators [2].
start_time = time.time()
acc = sum(x for x in range(0, 1000) if x % 3 == 0 or x % 5 == 0)
print(acc)
print(time.time() - start_time, "seconds")


# with list comprehensions
start_time = time.time()
acc = sum([x for x in range(0, 1000) if x % 3 == 0 or x % 5 == 0])
print(acc)
print(time.time() - start_time, "seconds")


# with lambda
start_time = time.time()
acc = sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(0, 1000)))
print(acc)
print(time.time() - start_time, "seconds")
