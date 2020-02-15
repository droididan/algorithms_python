import unittest
import medium


class MyTestCase(unittest.TestCase):
    def test_longestPelindromicSubstring(self):
        self.assertEqual(medium.longestPelindromicSubstring('abaxxaaxx'), 'xxaaxx')

    def test_searchInSortedMatrix(self):
        self.assertEqual(medium.searchInSortedMatrix(matrix, 4), [1, 0])
        self.assertEqual(medium.searchInSortedMatrix(matrix, 41), [1, 3])
        self.assertEqual(medium.searchInSortedMatrix(matrix, 1004), [5, 4])


if __name__ == '__main__':
    unittest.main()

matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]
