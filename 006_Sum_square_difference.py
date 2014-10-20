'''
Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

@author: Dos
'''
import time

def sum_square_difference(top):
    sum_of_the_square = 0
    tot_sum = 0
    
    for i in range(top+1):
        sum_of_the_square += i * i
        tot_sum += i
        print(i, sum_of_the_square, tot_sum)
    
    return tot_sum * tot_sum - sum_of_the_square


start_time = time.time()
print(sum_square_difference(100))
print(time.time() - start_time, "seconds")
