'''
Largest product in a grid

In the 2020 grid below, four numbers along a diagonal line have been marked
with '-'

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10-26-38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95-63-94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17-78-78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35-14-00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26  63  78  14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 2020 grid?

@author: Dos
'''

import timeit
import unittest


DIM = 4

GRID = "\
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n\
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n\
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n\
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n\
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n\
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n\
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n\
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n\
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n\
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n\
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n\
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n\
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n\
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n\
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n\
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n\
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n\
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n\
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n\
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"


# g = [ r.split() for r in GRID.split('\n')]
GRID = [ list(map(int,r.split())) for r in GRID.split('\n')]


class LargestProductInGrid():

    glob_max = 0

    def __init__(self, grid=GRID):
        self.grid = grid

    def set_grid(self, grid):
        self.grid = grid

    def set_max(self, glob_max):
        if glob_max > self.glob_max: self.glob_max = glob_max

    def max_prod_in_rows(self):
        for r in self.grid:
            for c in range(len(r)-DIM+1):
                self.set_max(r[c]*r[c+1]*r[c+2]*r[c+3])

    def max_prod_in_cols(self):
        for r in range(len(self.grid)-DIM+1):
            for c in range(len(self.grid[0])):
                self.set_max(self.grid[r][c]*self.grid[r+1][c]*self.grid[r+2][c]*self.grid[r+3][c])

    def max_prod_in_diags(self):

        # Diagonals bottom-right to top-left
        for r in range(len(self.grid)-DIM+1):
            for c in range(len(self.grid[0])-DIM+1):
                self.set_max(self.grid[r][c]*self.grid[r+1][c+1]*self.grid[r+2][c+2]*self.grid[r+3][c+3])

        # Diagonals bottom-left to top-right
        for r in range(DIM-1,len(self.grid)):
            for c in range(len(self.grid[0])-DIM+1):
                self.set_max(self.grid[r][c]*self.grid[r-1][c+1]*self.grid[r-2][c+2]*self.grid[r-3][c+3])

    def solve(self):
        self.max_prod_in_rows()
        self.max_prod_in_cols()
        self.max_prod_in_diags()




class TestLargestProductInGrid(unittest.TestCase):

    def setUp(self):
        self.lpg = LargestProductInGrid()

    def test_print_grid(self):
        self.assertEqual(self.lpg.grid[0][0],8)
        print(self.lpg.grid)

    def test_set_max(self):
        self.lpg.set_max(5)
        self.assertEqual(self.lpg.glob_max, 5)
        self.lpg.set_max(8)
        self.assertEqual(self.lpg.glob_max, 8)
        self.lpg.set_max(5)
        self.assertEqual(self.lpg.glob_max, 8)

    def test_max_prod_in_rows(self):
        self.lpg.max_prod_in_rows()
        self.assertTrue(self.lpg.glob_max > 0)
        self.assertTrue(self.lpg.glob_max == 48477312)

    def test_max_prod_in_cols(self):
        self.lpg.max_prod_in_cols()
        self.assertTrue(self.lpg.glob_max > 0)
        self.assertTrue(self.lpg.glob_max == 51267216)

    def test_max_prod_in_diags(self):
        self.lpg.max_prod_in_diags()
        self.assertTrue(self.lpg.glob_max > 0)
        self.assertTrue(self.lpg.glob_max == 70600674)

    def test_print_glob_max(self):
        self.lpg.max_prod_in_rows()
        print("global max: ", self.lpg.glob_max)
        self.lpg.max_prod_in_cols()
        print("global max: ", self.lpg.glob_max)
        self.lpg.max_prod_in_diags()
        print("global max: ", self.lpg.glob_max)



if __name__ == '__main__':
    unittest.main()

    # lpg = LargestProductInGrid()
    # lpg.solve()
    # print("global max: ", lpg.glob_max)