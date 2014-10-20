import time

__author__ = 'david'

'''
Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

@author: Dos
'''

import unittest
from primality_test import is_prime_Lucas_variation


FIRST_105_COMPOSITES = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38,
                        39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69,
                        70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99,
                        100, 102, 104, 105, 106, 108, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123,
                        124, 125, 126, 128, 129, 130, 132, 133, 134, 135, 136, 138, 140]


class Goldbach(object):
    evaluated_composites = []
    evaluated_primes = []
    evaluated_doubled_squares = []
    limit = 10000

    def solve_goldback(self, prime, square):
        return prime + 2 * square ** 2

    def is_composite(self, n):
        if n == 1:
            return False
        return not is_prime_Lucas_variation(n)

    def is_odd_composite(self, n):
        return n % 2 != 0 and self.is_composite(n)

    def are_composites(self, composites_list):
        for c in composites_list:
            if not self.is_composite(c):
                return False
        return True

    def solve(self):
        for i in range(self.limit):
            if self.is_odd_composite(i):
                self.evaluated_composites.append(i)
        print(self.evaluated_composites)

        for i in range(self.limit):
            if is_prime_Lucas_variation(i):
                self.evaluated_primes.append(i)
        print(self.evaluated_primes)

        doubled_square = 1
        i = 1
        while doubled_square < self.limit:
            doubled_square = 2*i**2
            i += 1
            self.evaluated_doubled_squares.append(doubled_square)
        print(self.evaluated_doubled_squares)

        for c in self.evaluated_composites:
            found = False
            for p in self.evaluated_primes:
                for ds in self.evaluated_doubled_squares:
                    if p + ds == c:
                        # print("%s + %s = %s" % (p, ds, c))
                        found = True
                        break
            if not found:
                print(c)
                break
        # else:
        #     self.limit *= 10
        #     self.solve()


class TestGoldbach(unittest.TestCase):
    def setUp(self):
        self.g = Goldbach()

    def test_solve_goldback(self):
        self.assertEqual(self.g.solve_goldback(7, 1), 9)
        self.assertEqual(self.g.solve_goldback(7, 2), 15)
        self.assertEqual(self.g.solve_goldback(3, 3), 21)
        self.assertEqual(self.g.solve_goldback(7, 3), 25)
        self.assertEqual(self.g.solve_goldback(19, 2), 27)
        self.assertEqual(self.g.solve_goldback(31, 1), 33)

    def test_is_composite(self):
        self.assertTrue(self.g.is_composite(4))
        self.assertTrue(self.g.is_composite(6))
        self.assertTrue(self.g.is_composite(8))
        self.assertTrue(self.g.is_composite(9))
        self.assertTrue(self.g.is_composite(10))
        self.assertTrue(self.g.is_composite(81))
        self.assertTrue(self.g.is_composite(91))
        self.assertTrue(self.g.is_composite(112))
        self.assertTrue(self.g.is_composite(138))
        self.assertFalse(self.g.is_composite(1))
        self.assertFalse(self.g.is_composite(11))
        self.assertFalse(self.g.is_composite(97))
        self.assertFalse(self.g.is_composite(131))

    def test_is_odd_composite(self):
        self.assertFalse(self.g.is_odd_composite(4))
        self.assertFalse(self.g.is_odd_composite(6))
        self.assertFalse(self.g.is_odd_composite(8))
        self.assertTrue(self.g.is_odd_composite(9))
        self.assertFalse(self.g.is_odd_composite(10))
        self.assertTrue(self.g.is_odd_composite(15))
        self.assertTrue(self.g.is_odd_composite(21))
        self.assertTrue(self.g.is_odd_composite(25))
        self.assertTrue(self.g.is_odd_composite(27))
        self.assertTrue(self.g.is_odd_composite(33))
        self.assertTrue(self.g.is_odd_composite(81))
        self.assertTrue(self.g.is_odd_composite(91))
        self.assertFalse(self.g.is_odd_composite(112))
        self.assertFalse(self.g.is_odd_composite(138))
        self.assertFalse(self.g.is_odd_composite(1))
        self.assertFalse(self.g.is_odd_composite(11))
        self.assertFalse(self.g.is_odd_composite(97))
        self.assertFalse(self.g.is_odd_composite(131))

    def test_are_composites(self):
        self.assertTrue(self.g.are_composites(FIRST_105_COMPOSITES))

    def test_solve(self):
        start_time = time.time()
        self.g.solve()
        print((time.time() - start_time)*1000 + "milliseconds")


if __name__ == '__main__':
    unittest.main()
