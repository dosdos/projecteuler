__author__ = 'david'

'''
Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 × 7  × 23
645 =   3 × 5  × 43
646 =   2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

@author: Dos
'''

import unittest
from primality_test import is_prime_Lucas_variation


class DistinctPrimeFactors(object):
    pass


class TestGoldbach(unittest.TestCase):
    def setUp(self):
        self.dpf = DistinctPrimeFactors()

    def test_lapalisse(self):
        self.assertTrue(1)


if __name__ == '__main__':
    unittest.main()
