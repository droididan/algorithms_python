import unittest
import easy


class Easy(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(easy.isPalindrome('abba'), True)
        self.assertEqual(easy.isPalindrome('azbba'), False)

    def test_two_sum_numbers(self):
        self.assertEqual(easy.twoNumberSum(arr, target), [14, -1])

    def test_bubble_sort(self):
        self.assertEqual(easy.bubbleSort([9, 2, 8, 1, 4, 3, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_selection_sort(self):
        self.assertEqual(easy.selectionSort([4, 2, 3, 1, 7, 5]), [1, 2, 3, 4, 5, 7])

    def test_product_sum(self):
        self.assertEqual(easy.productSum([1, 1, [1, 1], [1]]), 8)


arr = [10, 2, 14, -1, 2]
target = 13

if __name__ == '__main__':
    unittest.main()
