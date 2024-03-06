import unittest
from sorting import InsertionSort, MergeSort

class TrivialTest(unittest.TestCase):
    def test_true(self):
        print('Hello, welcome to the algorithm world!')
        self.assertTrue(True, "Test value is not true :(")

    def test_insertion_sort(self):
        self.assertEqual(InsertionSort([1, 4, 6, 2]), [1, 2, 4, 6])
        self.assertEqual(InsertionSort([10, 44, 6, 0, 1]), [0, 1, 6, 10, 44])
    
    def test_merge_sort(self):
        self.assertEqual(MergeSort([1, 4, 6, 2]), [1, 2, 4, 6])
        self.assertEqual(MergeSort([10, 44, 6, 0, 1]), [0, 1, 6, 10, 44])

if __name__ == '__main__':
    unittest.main()