'''
Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

@author: Dos
'''
import unittest


class CoinSum(object):
    coins = [200,100,50,20,10,5,2,1]
    target_sum = 200
    def __init__(self):
        pass

    def calculate(self):
        count = 0
        for c in self.coins:
            acc = 0
            while acc <= self.target_sum:
                acc += c



class Test(unittest.TestCase):
    def setUp(self):
        self.coinSum = CoinSum()

    def testCoins(self):
        self.assertEqual(self.coinSum.coins, [200,100,50,20,10,5,2,1])

    def testTargetSum(self):
        self.assertEqual(self.coinSum.target_sum, 200)


