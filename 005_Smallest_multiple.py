'''
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

@author: Dos
'''
import time


def prime_factors(n):
    factors = []  
    for i in range(2,int(n/2)+1):
        while n%i == 0:  
            factors.append(i)
            n = int(n/i)
    if len(factors) == 0:
        factors.append(n)
    return factors


def smallest_multiple(n):
    dict_mult = {}
    
    for i in range(2,n):
        dict_tmp = {}
        for j in prime_factors(i):
            if j in dict_tmp:
                dict_tmp[j] += 1
            else:
                dict_tmp[j] = 1
        
#         print('fattori di ',i,': ',dict_tmp)
        
        for j in dict_tmp.keys():
            if j in dict_mult:
                if dict_mult[j] < dict_tmp[j]:
                    dict_mult[j] = dict_tmp[j]
            else:
                dict_mult[j] = dict_tmp[j]
    
#     print(dict_mult)
    
    mult = 1
    for k in dict_mult.keys():
        for i in range(dict_mult[k]):
            mult *= k
    return mult


start_time = time.time()
print(prime_factors(120))
print(smallest_multiple(20))
print(time.time() - start_time, "seconds")

