'''
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91x99.

Find the largest palindrome made from the product of two 3-digit numbers.

@author: Dos
'''
import time

# palindrome with list index
def is_palindrome_list(n):
    s = str(n)
    match = True
    i = 0
    
    while match and i <= int(len(s)/2):
#         print(i, int(s[i]), int(s[-(i+1)]) )
        if int(s[i]) != int(s[-(i+1)]):
            match = False
        i += 1
    
    return match

# palindrome with reversed integers
def is_palindrome_reverse_int(n):
    return n==int(str(n)[::-1])

# palindrome with reversed strings
def is_palindrome_reverse_str(n):
    return str(n)==str(n)[::-1]

# is_palindrome_reverse_str is the fastest!!
def is_palindrome(n):
    return is_palindrome_list(n)


def largest_pal_prod():
    top_i = top_j = 999
    maximus = 0
    
    for i in range(top_i)[::-1]:
        for j in range(top_j)[::-1]:
            prod = i*j
    #         print(i,j,prod)
            if prod>maximus and is_palindrome(prod):
                maximus = prod
        top_j -= 1
    return maximus


start_time = time.time()
print(largest_pal_prod())
# print(is_palindrome_list(12345678909876543211234567890987654321))
# print(is_palindrome_list(123456789098765432113234567890987654321))
# print(is_palindrome_reverse_int(12345678909876543211234567890987654321))
# print(is_palindrome_reverse_int(123456789098765432113234567890987654321))
# print(is_palindrome_reverse_str(12345678909876543211234567890987654321))
# print(is_palindrome_reverse_str(123456789098765432113234567890987654321))
print(time.time() - start_time, "seconds")

